from fastapi import FastAPI, Request, Form,Depends
from fastapi.templating import Jinja2Templates
from utils.schemas import UserInput
from calc import BaseCalculator


app = FastAPI()

templates = Jinja2Templates(directory='templates')



@app.get('/')
def home(request : Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )






@app.post("/calc")
def calc(request : Request,
         a : float = Form(...),
         b : float = Form(...),
         choice : str = Form(...)):

    if choice == "add":
        result = BaseCalculator(a, b).add()
    elif choice == "sub":
        result = BaseCalculator(a, b).subtract()
    elif choice == "mul":
        result = BaseCalculator(a, b).multiply()
    elif choice == "div":
        result = BaseCalculator(a, b).divide()
    else:
        result = "Wrong Choice: Try Again!"


    return templates.TemplateResponse(request=request,
                                      name='index.html',
                                      context={
                                          "message" : "ok",
                                          "a" : a,
                                          "b" : b,
                                          "choice" : choice,
                                          "result" : result
                                      })