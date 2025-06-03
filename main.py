# main.py - Version minimale pour tester
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/test")
def read_test():
    return {"message": "You are in RCW!"}