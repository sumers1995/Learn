from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from services import get_answer

app = FastAPI()

@app.get("/invoke/")
def invoke_model(query: str):
    ans = get_answer(query)
    return {"Answer": ans}

@app.get("/")
def root():
    return {"message": "Langchain Demonstration"}

@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Langchain Demonstration"
    )