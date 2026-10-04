import streamlit as st
import os
from openai import OpenAI
import json
import datetime
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

# 保存会话信息函数
def session_save():
    # 构建保存的当前会话的json格式
    session_json = {
        "nickname": st.session_state.nickname,
        "personality": st.session_state.personality,
        "filename": st.session_state.filename,
        "messages": st.session_state.messages
    }
    
    if st.session_state.filename:
        # 如果sessions目录不存在，创建它
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
        # 保存当前会话
        with open(f"sessions/{st.session_state.filename}.json", "w",encoding="utf-8") as f:
            json.dump(session_json, f, ensure_ascii=False, indent=4)

# 定义要保存的会话名称
def session_filename():
    return f"{datetime.datetime.now().strftime('%Y-%m-%d-%H%M%S')}"

# 加载历史会话框信息函数
def sessions_load():
    session_list = []
    # 加载sessions目录下的所有文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        # 遍历所有文件，判断是否是json文件
        for file in file_list:
            if file.endswith(".json"):
                # 获取去掉后缀的文件名并添加到session_list
                file = file[:-5]
                session_list.append(file)
    return session_list

# 加载会话信息函数
def session_load(s_file):
    try:
        if os.path.exists(f"sessions/{s_file}.json"):
            with open(f"sessions/{s_file}.json", "r",encoding="utf-8") as f:
                session_json = json.load(f)
                st.session_state.nickname = session_json["nickname"]
                st.session_state.personality = session_json["personality"]
                st.session_state.filename = session_json["filename"]
                st.session_state.messages = session_json["messages"]
    except Exception:
        st.error(f"加载会话信息失败")

# 删除会话信息函数
def session_delete(s_file):
    try:
        if os.path.exists(f"sessions/{s_file}.json"):
            os.remove(f"sessions/{s_file}.json")
            st.success(f"会话{s_file}已删除")
            if s_file == st.session_state.filename:
                st.session_state.filename = session_filename()
                st.session_state.nickname = "夏美子"
                st.session_state.personality = "聪明可爱娇小的女孩"
                st.session_state.messages = []
    except Exception:
        st.error(f"删除会话{s_file}失败")


# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []
# 初始化昵称和性格
if 'nickname' not in st.session_state:
    st.session_state.nickname = "夏美子"
if 'personality' not in st.session_state:
    st.session_state.personality = "聪明可爱娇小的女孩"
if 'filename' not in st.session_state:
    st.session_state.filename = session_filename()



# 设置侧边栏 - with:streamlit里面的上下文管理器
with st.sidebar:
    # 新建会话
    if st.button("新建会话",width="stretch",icon="🔄"):
        # 1. 保存当前会话信息
        session_save()
        # 2.打开新会话
        # 2.1 判断当前会话是否为空，为空不创建新会话
        if st.session_state.messages:
            # 2.2 清空message列表，并生成新的文件名与初始化AI智能伴侣的昵称和性格
            st.session_state.messages = []
            st.session_state.nickname = "夏美子"
            st.session_state.personality = "聪明可爱娇小的女孩"
            st.session_state.filename = session_filename()
            # 2.3 保存新会话信息
            session_save()
            # 2.4 重新加载页面
            st.rerun()
        
    # 加载历史会话
    st.text("历史会话")
    session_list = sessions_load()
    for s in session_list:
        col1, col2 = st.columns([4,1])
        with col1:
            # 三元运算符：根据是否是当前会话，判断按钮的类型
            # 三元运算符格式：值1 if 条件 else 值2
            if st.button(s,width="stretch",icon="📃",key=s,type="primary" if s==st.session_state.filename else "secondary"):
                session_load(s)
                st.rerun()
        with col2:
            if st.button("",width="stretch",icon="❌",key=f"{s}_delete"):
                session_delete(s)
                st.rerun()


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
# 输出当前会话信息
st.text(f"当前会话：{st.session_state.filename}")

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

    # 保存当前会话信息--没完成一次互动，就保存一次会话信息
    session_save()
    