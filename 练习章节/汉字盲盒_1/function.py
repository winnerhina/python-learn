from datetime import datetime
from pydantic import BaseModel
from typing import Any
import json


# 生成会话ID
def create_session_id() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 保存会话数据
def save_session_data(session_id: str, session_data: dict) -> None:
    with open(f"sessions/{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

# 读取会话数据
def load_session_data(session_id: str) -> dict:
    with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
        return json.load(f) 

# 封装给后端实现聊天功能的请求参数
class ApiRequestChat(BaseModel):
    session_id: str
    message: str

# 封装返回给Web端的数据
class ApiResponse(BaseModel):
    code: int
    message: str
    date: Any = None
