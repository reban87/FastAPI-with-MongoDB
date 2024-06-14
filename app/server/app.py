from fastapi import FastAPI
from server.routes.student import router as StudentRouter

app = FastAPI()


app.include_router(StudentRouter, tags=["Students"], prefix="/student")


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Hello from app!"}
