from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    print("Server started...")
    yield
    print("...stopped!")

app = FastAPI(lifespan=lifespan_handler)

@app.get("/")
def root():
    print({"message": "Server is running..."})