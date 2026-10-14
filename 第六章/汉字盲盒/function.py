from datetime import datetime
import pydantic
from typing import Any



# 封装响应数据类
class ApiResponse(pydantic.BaseModel):
    code: int
    message: str
    date: Any

# 生成会话标识
def create_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
