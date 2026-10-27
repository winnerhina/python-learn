from datetime import datetime
from pydantic import BaseModel
from typing import Any
import json

# 生成会话标识
def get_session_id() -> str:
    """
    生成会话标识
    :return: 会话标识字符串，格式为YYYY-MM-DD_HH-MM-SS
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 保存聊天数据json文件到本地
def save_session_data(session_data: dict, session_id: str) -> None:
    """
    保存会话数据到本地json文件
    :param session_data: 会话数据字典，包含会话标识和消息列表
    :return: 无返回值
    """
    with open(f"sessions/{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

# 加载聊天数据
def load_session_data(session_id: str) -> dict:
    """
    从本地json文件加载会话数据
    :param session_id: 会话标识
    :return: 会话数据字典，包含会话标识和消息列表
    """
    try:
        with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
            session_data = json.load(f)
            return session_data
    except FileNotFoundError:
        return {
            "session_id": session_id,
            "messages": []
        }
# 定义Chat接收来自Web端的请求参数，并转换为对象格式
class ApiRequest(BaseModel):
    message: str
    session_id: str

# 定义返回给Web端的返回数据格式
class ApiResponse(BaseModel):
    code: int
    message: str
    data: Any 
