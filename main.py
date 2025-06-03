from fastapi import FastAPI, HTTPException
 
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()
 
@app.get("/")
async def welcome():
    try:
        return {"message": "Welcome to the FastAPI application!"}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail= str(e))
   
@app.get("/test")
async def welcome():
    try:
        return {"message": "You are in RCW!"}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail= str(e))