# 🏦 Bank Customer Churn Prediction API

A lightweight, production-ready **FastAPI** service for predicting whether a customer will leave a bank. Built with a pre-trained **Support Vector Classifier (SVC)** and transformer for real-time inference. Clean, testable, and MLflow-ready.

---

## 🚀 What’s Inside

- 🔮 **Prediction Endpoint**: Returns churn prediction and probability.
- ✅ **Health Check**: Instantly check API status.
- 🏠 **Home**: Friendly welcome route.
- 🔁 **MLflow Integration**: Tracks inputs & predictions.
- 🧪 **Tests**: Fully tested endpoints with `pytest`.

---

## 🔧 Setup Instructions

### 📦 Requirements

- Python 3.12+
- MLflow server (optional, for logging)
- Pre-trained model: `SVC_classifier.pkl`
- Transformer: `transformer.pkl`

### 🛠️ Installation

```bash
git clone <your-repo-url>
cd MLOPS-COURSE-LABS

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

---

## ▶️ Running the API

Make sure the model and transformer are placed in:

```
mlruns/models/
├── SVC_classifier.pkl
└── transformer.pkl
```

Then start the FastAPI app:

```bash
uvicorn app:app --reload
```

API is now live at: [http://localhost:8000](http://localhost:8000)

---

## 📡 API Endpoints

| Method | Endpoint     | Description             |
|--------|--------------|-------------------------|
| GET    | `/`          | Home route              |
| GET    | `/health`    | API health status       |
| POST   | `/predict`   | Predict customer churn  |

### 🔍 Sample Predict Request

```json
POST /predict
Content-Type: application/json

{
  "credit_score": 720,
  "geography": "Germany",
  "gender": "Female",
  "age": 36,
  "tenure": 5,
  "balance": 82000,
  "num_of_products": 1,
  "has_cr_card": 1,
  "is_active_member": 1,
  "estimated_salary": 65000
}
```

### ✅ Sample Response

```json
{
  "churn_prediction": 1,
  "probability": 0.81,
  "message": "Prediction successful"
}
```

---

## 🧪 Testing

```bash
pytest tests/ -v
```

Expected Output:

```
✅ test_home_endpoint
✅ test_health_endpoint
✅ test_predict_endpoint
```

---

## 🌱 Project Layout

```
LAb3/
├── main.py                  # FastAPI app
├── model/
│   └── svc_model.pkl        # Trained SVC model
├── data/
│   └── Churn_Modelling.csv  # Original dataset
├── utils/
│   ├── logger.py            # Logging setup
├── tests/
│   └── test_api.py
├── requirements.txt 
└── README.md

```

---

## 📊 MLflow (Optional)

Run MLflow server locally:

```bash
mlflow server --host 0.0.0.0 --port 5000
```

Then visit [http://localhost:5000](http://localhost:5000) to explore experiment logs.

---

## 🧾 Dependencies

Major libraries used:

- fastapi
- uvicorn
- pandas
- scikit-learn
- joblib
- mlflow
- httpx
- pytest

---

## 📝 Notes

- Update `app.py` if your MLflow server is remote.
- You can replace the SVC model with another classifier if retraining.
- `Churn_Modelling.csv` is only for reference; it's not needed to run the API.
