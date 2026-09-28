import streamlit as st
import os
from openai import OpenAI


# 设置页面的配置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="ai_partner_resources/logo.png",
    # 布局
    layout="wide",
    # 控制侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 调用大模型进行交互
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY_1'),base_url="https://api.deepseek.com")

# 系统提示词
system_prompt = "你是一名带有温柔聪明可爱娇娇属性的女孩，名字为神乐。"

# 导入logo
st.logo("ai_partner_resources/logo.png")

# 大标题
st.title("AI智能伴侣")

# 聊天输入框
input_text = st.chat_input("请输入您要和AI智能伴侣的互动内容：")
if input_text:
    st.chat_message("user").write(input_text)
    print("-------------->调用ai大模型：\n", input_text)
    # 与ai大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("<-------------大模型返回的结果：\n", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)