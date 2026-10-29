from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    handlers=[
        logging.StreamHandler(logging.stdout),
        logging.FileHandler("app.log", encoding="utf-8")
    ]
)

app = FastAPI()

@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception) -> JSONResponse:
    logging.error(f"Exception in {request.url.path}: {exc}")
    return JSONResponse(status_code=500, content={"code": 500, "message": str(exc), "data": None})
