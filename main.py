from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return "Hello FastAPI"


@app.get("/url")
async def root2():
    return {"message": "Hello FastAPI"}
