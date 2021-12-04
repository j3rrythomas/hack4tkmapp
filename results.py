from fastapi import FastAPI, HTTPException
from model import predict
import json

# prediction_list =predict()
# print(type(prediction_list))

app = FastAPI()

@app.get("/predict",status_code=200)
def get_prediction():

    prediction_list = predict()

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    return {'status': 'ok', 'json_data': prediction_list}
# @app.post("/")
