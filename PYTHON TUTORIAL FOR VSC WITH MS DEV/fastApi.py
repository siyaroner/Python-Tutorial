from fastapi import FastAPI 
app= FastAPI()

@app.get("/") # get is a end point. And we have get, post, put, delete main end point
def home():
    return {"Data":"Test"}
