import time

from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    type1 = "type1"
    type2 = "type2"
    type3 = "type3"
    type4 = "type4"
    type5 = "type5"


app = FastAPI()


@app.get("/")
async def root():
    # return {"message": "You are in the root"}
    # return {"message": "You are at home"}
    return {"message": "You are at the right place"}


@app.get("/item/{item_id}")
async def read_item(item_id):
    if item_id == "1":
        return {"item_id": item_id, "message": "test 1"}
    if item_id == "2":
        return {"item_id": item_id, "message": "test 2"}

    return {"item_id": item_id}


@app.get("/predict/{predict_type}")
async def get_model(predict_type: ModelName):
    if predict_type == ModelName.type1:
        return {"predict_type": predict_type, "message": "prediction type1"}

    if predict_type == ModelName.type2:
        return {"predict_type": predict_type, "message": "prediction type2"}

    if predict_type == ModelName.type3:
        return {"predict_type": predict_type, "message": "prediction type3"}

    return {"predict_type": predict_type, "message": "General recommendation"}


@app.get("/timeout")
async def read_item(wait_sec: int):
    time.sleep(120)
    return {"message": "Success"}


@app.get("/timeout/{wait_sec}")
async def read_item(wait_sec: int):
    time.sleep(wait_sec)
    return {"message": "Success"}

# pip install "fastapi[all]"
# or
# pip install fastapi  + # pip install "uvicorn[standard]"
# or
# pip install fastapi + # pip install uvicorn

# run server: $ uvicorn main:app --reload

# url: http://127.0.0.1:8000
# JSON (schema): http://127.0.0.1:8000/openapi.json
# Option 1 API docs 'swagger': http://127.0.0.1:8000/docs
# Option 2 API docs 'redoc': http://127.0.0.1:8000/redoc
