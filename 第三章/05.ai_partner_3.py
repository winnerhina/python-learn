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
# 初始化昵称和性格
if 'nickname' not in st.session_state:
    st.session_state.nickname = "神乐"
if 'personality' not in st.session_state:
    st.session_state.personality = "聪明可爱娇小的傲娇萝莉女孩"


# 设置侧边栏 - with:streamlit里面的上下文管理器
with st.sidebar:
    st.subheader("定制专属你的AI智能伴侣")
    # 昵称输入框
    nickname = st.text_input("请定义AI智能伴侣的昵称：", value=st.session_state.nickname,placeholder="请输入您的昵称")
    # 性格输入框
    personality = st.text_input("请定义AI智能伴侣的性格：", value=st.session_state.personality,placeholder="请输入您的性格")

    # 记录用户输入
    st.session_state.nickname = nickname
    st.session_state.personality = personality



# 调用大模型进行交互
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY_1'),base_url="https://api.deepseek.com")

# 系统提示词
system_prompt = f"""
# 你叫{nickname}，现在是用户的真实伴侣，请完全代入伴侣角色。
规则：
    1. 每次只回1条消息
    2. 匹配用户的语言
    3. 回复简短，像微信聊天一样
    4. 有需要的话可以用❤️🌸等emoji表情
    5. 用符合伴侣性格的方式对话
    6. 回复的内容，要充分体现伴侣的性格特征
    7. 聊天时候可以展示出内心活动
伴侣性格：
    - {personality}
你必须严格遵守上述规则来回复用户。
"""

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