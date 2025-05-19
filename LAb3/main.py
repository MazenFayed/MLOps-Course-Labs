from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import logging
import mlflow
from utils.logger import setup_logger
import joblib

app = FastAPI()
logger = setup_logger("churn_api_logger")

# Load model
with open(r"E:\Courses\MLops\Labs\lab3\models\svm_churn_model.pkl", "rb") as f:
    model = joblib.load(f)

# Input schema
class CustomerInput(BaseModel):
    credit_score: int
    geography: str
    gender: str
    age: int
    tenure: int
    balance: float
    num_of_products: int
    has_cr_card: int
    is_active_member: int
    estimated_salary: float

@app.get("/")
def home():
    logger.info("Home endpoint hit.")
    return {"message": "Bank Churn Prediction API"}

@app.get("/health")
def health():
    logger.info("Health check endpoint hit.")
    return {"status": "ok"}

@app.post("/predict")
def predict(data: CustomerInput):
    try:
        logger.info(f"Received prediction request: {data}")
        # Assume preprocessing converts input into correct vector
        input_vector = [[
            data.credit_score,
            1 if data.geography == 'France' else 0,
            1 if data.gender == 'Male' else 0,
            data.age,
            data.tenure,
            data.balance,
            data.num_of_products,
            data.has_cr_card,
            data.is_active_member,
            data.estimated_salary
        ]]
        prediction = model.predict(input_vector)[0]

        # Log to MLflow
        mlflow.set_experiment("Churn API Predictions")
        with mlflow.start_run():
            mlflow.log_params(data.dict())
            mlflow.log_metric("prediction", prediction)

        logger.info(f"Prediction: {prediction}")
        return {"churn_prediction": int(prediction)}
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return {"error": str(e)}
