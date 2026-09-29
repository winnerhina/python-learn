import streamlit as st
import os
from openai import OpenAI

# 日志
print("-------------->开始运行AI智能伴侣：\n")
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

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 调用大模型进行交互
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY_1'),base_url="https://api.deepseek.com")

# 系统提示词
system_prompt = "你是一名带有温柔聪明可爱娇娇属性的女孩，名字为神乐。"

# 导入logo
st.logo("ai_partner_resources/logo.png")

# 大标题
st.title("AI智能伴侣")

# 输出聊天历史
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 聊天输入框
input_text = st.chat_input("请输入您要和AI智能伴侣的互动内容：")
if input_text:
    st.chat_message("user").write(input_text)
    # 记录用户输入
    st.session_state.messages.append({"role": "user", "content": input_text})
    # 日志
    print("-------------->调用ai大模型：\n", input_text)

    # 与ai大模型进行交互
    print(st.session_state.messages)  # 日志

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            # 解包聊天历史，使得大模型拥有记忆功能。
            *st.session_state.messages,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果（非流失输出
    # print("<-------------大模型返回的结果：\n", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回的结果（流失输出）
    response_message = st.empty()  # 创建空容器用于显示大模型返回的结果（流失输出）的实时内容
    content = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content += chunk.choices[0].delta.content
            response_message.chat_message("assistant").write(content)
    # 记录大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": content})