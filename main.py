from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import uvicorn

# Initialize FastAPI app
app = FastAPI()


# Define request body schema using Pydantic BaseModel
class sepsisFeatures(BaseModel):
    PRG: float
    PL: float
    PR: float
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: int
    Insurance: int


# Define machine learning models Classes
class NaiveBayes:
    def __init__(self):
        # Load trained naive bayes model
        with open("./models/nb_pipeline.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, data):
        # Implement prediction logic for naive bayes model
        return self.model.predict(data)


class LogRegression:
    def __init__(self):
        # Load trained Logistic regression model
        with open("./models/lr_pipeline.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, data):
        # Implement prediction logic for Logistic regression
        return self.model.predict(data)


class RanddomForest:
    def __init__(self):
        # Load trained random forest model
        with open("./models/rf_pipeline.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, data):
        # Implement prediction logic for random forest
        return self.model.predict(data)


# Initialize your machine learning models
nb_model = NaiveBayes()
lr_model = LogRegression()
rf_model = RanddomForest()


# Define endpoint for prediction with model 1
@app.post("/predict/naive_bayes")
def predictNaiveBayes(data: sepsisFeatures):

    # convert data to dict and then to dataFrame
    df = pd.DataFrame([data.model_dump()])
    prediction = nb_model.predict(df)

    return {"prediction": prediction}


# Define endpoint for prediction with model 2
@app.post("/predict/logistic_regression")
def predictLogisticRegression(data: sepsisFeatures):

    # convert data to dict and then to dataFrame
    df = pd.DataFrame([data.model_dump()])
    prediction = lr_model.predict(df)

    return {"prediction": prediction}


# Define endpoint for prediction with model 3
@app.post("/predict/random_forest")
def predictRandomForest(data: sepsisFeatures):

    # convert data to dict and then to dataFrame
    df = pd.DataFrame([data.model_dump()])
    prediction = rf_model.predict(df)

    return {"prediction": prediction}


# Define homepage endpoint
@app.get("/")
def homepage():
    return {"message": "Welcome to the ML Model API!"}


# Run FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
