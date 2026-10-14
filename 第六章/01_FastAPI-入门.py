"""
----------------------------------FastAPI-入门----------------------------------

1.FastAPI是一个现代，快速高性能的Web框架，用于基于Python类型提示构建API接口服务。

2.API接口：应用程序编程接口，就是对外提供功能入口，供别人来调用

3.使用步骤：
   (1)导入FastAPI
   (2)创建FastAPI实例对象
   (3)创建路径操作函数，定义访问路径
   (4)运行FastAPI服务

4.运行命令（三种种方式任选其一）：
   fastapi dev "xxxx.py"
   uvicorn xxxx:app --reload   （app为实例对象名称）
   uvicorn.run(app, host="127.0.0.1", port=8000)-----卸载python代码里

5.示例代码：
   from fastapi import FastAPI

   # 创建FastAPI实例
   app = FastAPI()

   # 定义功能接口
   @app.get("/")
   def root():
       return {"message": "Hello World"}

   # 定义功能接口
   @app.get("/users")
   def get_users():
       return [{"id": 1, "name": "Alice", "age": 18},
               {"id": 2, "name": "Bob", "age": 20}]

    if __name__ == "__main__":
        uvicorn.run(app, host="127.0.0.1", port=8000)
"""

from fastapi import FastAPI

# 创建FastAPI实例
app = FastAPI()

# 定义功能接口(api接口)---》函数的返回值表示API接口的响应数据，接口的路径为"/"，请求方法为GET
@app.get("/")
def root():
    return {"message": "Hello World"}

# 定义功能接口(api接口)---》函数的返回值表示API接口的响应数据，接口的路径为"/users"，请求方法为GET
@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Alice", "age": 18},
            {"id": 2, "name": "Bob", "age": 20}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
