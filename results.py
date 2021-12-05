from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic.errors import NumberNotGeError
from model import predict
from pydantic import BaseModel
import json
import random

# prediction_list =predict()
# print(type(prediction_list))


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Info(BaseModel):
    time:str
    date:str
    # global_reactive_power: float
    # voltage: float

@app.get("/predict")
def pong():
    return {"ping": "pong!"}

@app.post("/predict",status_code=200)
def get_prediction(info:Info):
    voltage = random.uniform(230,250)
    global_reactive_power = random.uniform(0.0,1.39)
    result = predict(info.time,info.date,global_reactive_power,voltage)

    print(result)
    if not result:
        raise HTTPException(status_code=400, detail="Model not found.")

    return {'status':'ok','result':result[0] }
# @app.post("/")


