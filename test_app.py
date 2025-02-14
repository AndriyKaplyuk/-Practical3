import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_postdata_summ():
    response = client.post("/postdata", data={"number1": 1, "act": "summ", "number2": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_postdata_minus():
    response = client.post("/postdata", data={"number1": 5, "act": "minus", "number2": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_postdata_mult():
    response = client.post("/postdata", data={"number1": 3, "act": "mult", "number2": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 12.0}

def test_postdata_div():
    response = client.post("/postdata", data={"number1": 8, "act": "div", "number2": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}

def test_postdata_invalid_operation():
    response = client.post("/postdata", data={"number1": 5, "act": "invalid", "number2": 2})
    assert response.status_code == 200
    assert response.json() == {"result": "Operation impossible"}
