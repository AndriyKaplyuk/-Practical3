from fastapi.testclient import TestClient
from main import app  # Замініть на свій файл

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_postdata():
    response = client.post("/postdata", data={"number1": 5, "number2": 3, "act": "summ"})
    assert response.status_code == 200
    assert response.json() == {"result": 8.0}
