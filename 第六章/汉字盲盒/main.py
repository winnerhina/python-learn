from fastapi.responses import FileResponse
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
import json


import function
import AI_interaction



# 创建FastAPI实例
app = FastAPI(title="汉字盲盒")

# 配置静态文件目录
# 任何以"/static"开头的；路由请求都从"static"目录中查找对应的文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 保存会话数据到本地sessions目录
if not os.path.exists("sessions"):
    os.makedirs("sessions")

# 创建路径操作函数
@app.get("/")
def root():
    print("访问项目首页")
    return FileResponse("static/index.html")

# 创建新建会话路由
@app.post("/api/sessions")
def create_session() -> function.ApiResponse:
    print("创建新会话")
    # 1.生成会话ID
    session_id = function.create_session_id()

    # 2.构造会话数据，并保存到sessions目录
    session_data = {
        "session_id": session_id,
        "messages": []
    }
    with open(f"sessions/{session_id}.json", "w") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

    # 3.返回响应数据(封装为对象)
    return function.ApiResponse(code=200, message="会话创建成功", date=session_id)

# 创建聊天路由
@app.post("/api/chat")
def chat(request:function.ApiRequest) -> function.ApiResponse:
    print(f"<-----------------与AI互动：{request.session_id} : {request.message}")

    # 逻辑实现
    messages = AI_interaction.get_ai_response(request.session_id, request.message)

    # 7.给前端响应数据
    return function.ApiResponse(code=200, message="聊天成功", date=messages)




# 运行FastAPI应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
