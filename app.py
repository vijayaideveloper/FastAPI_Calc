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
        return {"a" : value.a,
                "b" : value.b,
                "Choice" : value.choice,
                "Result" : BaseCalculator(value.a, value.b).add()}
    if value.choice == 'sub':
        return {"a" : value.a,
                "b" : value.b,
                "Choice" : value.choice,
                "Result" : BaseCalculator(value.a, value.b).subtract()}
    if value.choice == 'mul':
        return {"a" : value.a,
                "b" : value.b,
                "Choice" : value.choice,
                "Result" : BaseCalculator(value.a, value.b).multiply()}
    if value.choice == 'div':
        return {"a" : value.a,
                "b" : value.b,
                "Choice" : value.choice,
                "Result" : BaseCalculator(value.a, value.b).divide()}
    else:
        return {"a" : value.a,
                "b" : value.b,
                "Choice" : f"Wrong Choice {value.choice}",
                "Result" : "Failed : Try again !"}
    