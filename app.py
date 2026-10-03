from fastapi import FastAPI
from utils.schemas import UserInput
from calc import BaseCalculator
app = FastAPI()

@app.get("/health")
def health_check():
    return {"message": "Hello, World!"}


@app.post("/calc")
def calc(value : UserInput):

    if value.choice == 'add':
        return {"message" : "ok",
                "a" : value.a,
                "b" : value.b,
                "choice" : value.choice,
                "result" : BaseCalculator(value.a, value.b).add()}
    if value.choice == 'sub':
        return {"message" : "ok",
                "a" : value.a,
                "b" : value.b,
                "choice" : value.choice,
                "result" : BaseCalculator(value.a, value.b).subtract()}
    if value.choice == 'mul':
        return {"message" : "ok",
                "a" : value.a,
                "b" : value.b,
                "choice" : value.choice,
                "result" : BaseCalculator(value.a, value.b).multiply()}
    if value.choice == 'div':
        return {"message" : "ok",
                "a" : value.a,
                "b" : value.b,
                "choice" : value.choice,
                "result" : BaseCalculator(value.a, value.b).divide()}
    else:
        return {"message" : "ok",
                "a" : value.a,
                "b" : value.b,
                "choice" : f"Wrong Choice {value.choice}",
                "result" : "Failed : Try again !"}
    