from fastapi import FastAPI

app = FastAPI()


@app.get("/books")
async def first_api():
    return {'hello': "world"}
