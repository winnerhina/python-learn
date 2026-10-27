from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import logging
import sys
import os

import function
import AI_interaction

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    handlers=[
            # handlers：日志的"出口"列表，可以同时挂多个，每挂一个日志就多写一份
            logging.StreamHandler(sys.stdout), 
            logging.FileHandler("app.log", encoding="utf-8")  
        ]
    )
# 创建汉字盲盒实例
app = FastAPI(title="汉字盲盒")

# 判断会话数据保存目录是否存在，不存在就创建
if not os.path.exists("sessions"):
    os.makedirs("sessions")

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"))

# 创建汉字盲盒首页路由
@app.get("/")
def game_root() -> FileResponse:
    logging.info("用户访问了首页")
    return FileResponse("static/index.html")

# 定义新建会话路由
@app.post("/api/sessions")
def create_sessions() -> function.ApiResponse:
    logging.info("用户创建了会话")
    # 获取会话标识
    session_id = function.get_session_id()
    # 构造会话数据结构
    session_data = {
        "session_id": session_id,
        "messages": []
    }
    # 保存会话数据到本地文件
    function.save_session_data(session_data, session_id=session_id)
    return function.ApiResponse(code=200, message="会话创建成功", data=session_data)

# 定义聊天路由
@app.post("/api/chat")
def chat(request: function.ApiRequest) -> function.ApiResponse:
    logging.info(f"<------------------ 用户向AI大模型发送了消息：{request.message}")
    # 核心逻辑实现
    response = AI_interaction.chat_with_ai(request.message, request.session_id)

    logging.info(f"------------------> AI大模型回复了：{response}")

    return function.ApiResponse(code=200, message="消息发送成功", data=response)

# 定义加载会话列表路由
@app.get("/api/sessions")
def load_sessions() -> function.ApiResponse:
    logging.info("加载了会话列表")
    # 获取所有会话文件列表
    session_list = os.listdir("sessions")
    # 去掉文件扩展名
    session_list = [session.split(".")[0] for session in session_list]
    # 倒序排序
    session_list.sort(reverse=True)
    return function.ApiResponse(code=200, message="会话列表加载成功", data=session_list)

# 定义删除会话路由
@app.delete("/api/sessions/{session_id}")
def delete_session(session_id: str) -> function.ApiResponse:
    if not os.path.exists(f"sessions/{session_id}.json"):
        return function.ApiResponse(code=404, message="会话数据不存在", data=None)
    logging.info(f"用户删除了会话：{session_id}")
    # 删除会话数据文件
    os.remove(f"sessions/{session_id}.json")
    return function.ApiResponse(code=200, message="会话删除成功",data=None)

# 定义加载历史消息路由
@app.get("/api/sessions/{session_id}")
def load_messages(session_id: str) -> function.ApiResponse:
    logging.info(f"用户加载了会话：{session_id}的历史消息")
    # 从本地文件加载会话数据
    session_data = function.load_session_data(session_id=session_id)
    return function.ApiResponse(code=200, message="会话历史消息加载成功", data=session_data["messages"])



# 定义捕获全局异常
@app.exception_handler(Exception)
def handle_exception(request, exc):
    logging.error(f"异常的请求：{request.url}，异常信息：{exc}")
    return JSONResponse(status_code=500, content={"code": 500, "message": "服务器内部错误", "data": None})
