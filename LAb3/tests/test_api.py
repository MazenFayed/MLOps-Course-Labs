from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    res = client.get("/")
    assert res.status_code == 200
    assert "Bank Churn Prediction API" in res.text

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_predict():
    payload = {
        "credit_score": 600,
        "geography": "France",
        "gender": "Male",
        "age": 40,
        "tenure": 3,
        "balance": 60000.0,
        "num_of_products": 2,
        "has_cr_card": 1,
        "is_active_member": 1,
        "estimated_salary": 50000.0
    }
    res = client.post("/predict", json=payload)
    assert res.status_code == 200
    assert "churn_prediction" in res.json()
