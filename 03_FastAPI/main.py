import time
from typing import Callable

from fastapi import Body, FastAPI, Request, Response
from starlette.background import BackgroundTask

from .log_config import logger  # type: ignore

app = FastAPI()

def log_info(log_data):
    logger.info("Log Data", extra = log_data)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable):
    start_time = time.time()
    request_body = await request.body()
    response: Response = await call_next(request)
    response_body = b''
    async for chunk in response.body_iterator: # type: ignore
        response_body += chunk

    process_time = time.time() - start_time
    log_data = {
        "latency": process_time,
        "request": request_body.decode(),
        "method": request.method,
        "response": response_body.decode(),
        "metrics": "accuracy"
    }
    task = BackgroundTask(log_info, log_data)
    return Response(
        content = response_body,
        status_code = response.status_code, 
        headers = dict(response.headers), 
        media_type = response.media_type, 
        background = task
    )

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application"}

@app.post("/upload_vide/")
async def upload_video(video_url: str = Body(...)):
    time.sleep(1) # Simulating waiting time
    return {"status": f"uploaded to {video_url}"}

