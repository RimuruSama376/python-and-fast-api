from fastapi import FastAPI

app = FastAPI()


@app.get("/test-api")
async def root():
    return {"message": "Hello World"}