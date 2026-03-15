from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

#creating object of fastapi
app = FastAPI()
#pickle file
model = joblib.load("model.pkl")


class IrisInput(BaseModel):
    data: list


@app.get("/")
def home():
    return {"message": "ML Model API running"}


@app.post("/predict")
def predict(input: IrisInput):

    data_array = np.array(input.data).reshape(1, -1)

    prediction = model.predict(data_array)

    return {"prediction": int(prediction[0])}