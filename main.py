from fastapi import FastAPI
from rutas import router
app = FastAPI()

@app.get("/")
def root():
    return{"Server message":"Conect"}

app.include_router(router)




