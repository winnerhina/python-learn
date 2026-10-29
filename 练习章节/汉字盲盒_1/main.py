from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os
import logging
import sys


import function
import AI_interaction


# 配置日志记录：同时输出到控制台(stdout)和 app.log 文件
# 作用：logging.info() 打出来的日志，往哪写、写多详细、长什么样，都由这里统一决定
logging.basicConfig(
    level=logging.INFO,  # level：只记录 INFO 及以上级别的日志（INFO/WARNING/ERROR），DEBUG 太啰嗦不记录
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    # format：日志的排版模板。依次是 时间 - 级别 - 哪个文件哪一行 - 日志内容，方便定位是哪个接口打的
    handlers=[
        # handlers：日志的"出口"列表，可以同时挂多个，每挂一个日志就多写一份
        logging.StreamHandler(sys.stdout),  # 出口1：写入标准输出 stdout（终端/预览控制台，和 print 同一通道）
        logging.FileHandler("app.log", encoding="utf-8")  # 出口2：同时写入 app.log 文件，方便事后翻查；utf-8 防止中文乱码
    ]
)

# 创建FastAPI实例
app = FastAPI(title="汉字盲盒")

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 定义会话数据保存目录
if not os.path.exists("sessions"):
    os.makedirs("sessions")

# 定义汉字盲盒首页路由
@app.get("/")
def root():
    logging.info("访问项目首页")
    return FileResponse("static/index.html")

# 定义汉字盲盒新建会话路由
@app.post("/api/sessions")
def create_session() -> function.ApiResponse:
    logging.info("创建新会话")
    # 1.生成会话ID
    session_id = function.create_session_id()
    
    # 2.构造会话数据
    session_data = {
        "session_id": session_id,
        "messages": []
    }

    # 3.保存会话数据
    function.save_session_data(session_id, session_data)
    
    # 4.返回响应数据(封装为对象)
    return function.ApiResponse(code=200, message="会话创建成功", date=session_id)
# 定义汉字盲盒查看历史会话路由
@app.get("/api/sessions")
def get_sessions() -> function.ApiResponse:
    logging.info("查看历史会话")
    # 1.获取所有会话文件
    sessions_lt = [session for session in os.listdir("sessions") if session.endswith(".json")]
    # 2.去掉".json"后缀名
    sessions_list = [session.split(".")[0] for session in sessions_lt]
    # 3.按倒序排序
    sessions_list.sort(reverse=True)
    # 4.返回响应数据(封装为对象)
    return function.ApiResponse(code=200, message="会话列表成功", date=sessions_list)
# 定义汉字盲盒聊天功能实现路由
@app.post("/api/chat")
def chat(request:function.ApiRequestChat) -> function.ApiResponse:
    logging.info(f"<-----------------与AI互动：{request.session_id} : {request.message}")
    # 功能实现：与AI互动，获取回复消息
    response = AI_interaction.interact_with_AI(request.message, request.session_id)
    logging.info(f"----------------->AI返回：{request.session_id} : {response}")
    return function.ApiResponse(code=200, message="聊天成功", date=response)
# 定义加载历史会话聊天信息路由
@app.get("/api/sessions/{session_id}")
def get_session(session_id: str) -> function.ApiResponse:
    logging.info(f"加载会话数据：{session_id}")
    # 1.加载会话数据
    session_data = function.load_session_data(session_id)
    # 2.返回响应数据(封装为对象)
    return function.ApiResponse(code=200, message="会话数据加载成功", date=session_data["messages"])
# 定义删除历史会话路由
@app.delete("/api/sessions/{session_id}")
def delete_session(session_id: str) -> function.ApiResponse:
    logging.info(f"删除会话数据：{session_id}")
    # 1.删除会话数据
    if not os.path.exists(f"sessions/{session_id}.json"):
        return function.ApiResponse(code=404, message="会话数据不存在", date=session_id)
    os.remove(f"sessions/{session_id}.json")
    # 2.返回响应数据(封装为对象)
    return function.ApiResponse(code=200, message="会话数据删除成功", date=session_id)

# 定义全局异常捕获路由
@app.exception_handler(Exception)
def handle_exception(request, exc):
    logging.error(f"请求路径{request.url} 异常捕获：{exc}")
    return JSONResponse(content={"code": 500, "message": str(exc)})
# 运行FastAPI应用
if __name__ == "__main__":
    import uvicorn
    # log_config=None：不让 uvicorn 接管日志配置，否则会覆盖上面 basicConfig 的设置，导致 logging.info 不输出
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", log_config=None)
    