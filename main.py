from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class student(BaseModel):
    Reference:str
    FirstName:str
    LastName:str
    Age:int

@app.get("/hello",status_code=200)
def read_hello():
    return "Hello world"

@app.get("/welcome",status_code=200 )
def welcome_user(name: str):
    return {"message":f"welcome {name}"}

class student(BaseModel):
    Reference:str
    FirstName:str
    LastName:str
    Age:int