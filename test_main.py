from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "You are in the root"}


def test_read_item():
    response = client.get("/item/2")
    assert response.status_code == 200
    assert response.json() == {"item_id": "2", "message": "test 2"}


def test_read_predict():
    response = client.get("/predict/type3")
    assert response.status_code == 200
    assert response.json() == {"predict_type": "type3", "message": "prediction type3"}


