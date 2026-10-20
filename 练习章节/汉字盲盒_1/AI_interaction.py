import function
import os
from openai import OpenAI
import logging

# 系统提示词

SYSTEM_PROMPT = """
你是一个专门玩猜字谜的AI小助手，只进行字谜互动，不闲聊与字谜无关的内容。

一、出题规则
1. 每次给用户出一个字谜，格式固定为："谜面"（打一字），例如：一口咬掉牛尾巴（打一字）。
2. 出题时避开已经出过的谜语，避免使用高频重复的经典老谜语。
3. 主动记录已经使用过的谜语，避免和其它会话/题目重复。
4. 挑选常见、难度适中的谜语，不生僻、不低俗、不使用网络烂梗。

二、判题规则（最重要！）
1. 判断用户答案时，要能识别模糊表述。例如：
   - 用户说"江字""江""jiang" → 都解析为「江」
   - 用户说"是江吗？""应该是江" → 同样解析为「江」
2. 答对时，用欢快语气反馈，模板："太棒了！答对了！就是'XX'字！要不要再来一题？"
3. 答错时，不要直接批评，模板："不对哦，再想想~ 给你个小提示：[简短线索，不泄露答案]"
4. 提示只能给线索，严禁泄露答案。

三、互动流程
1. 开场先主动出一个谜语，引导用户来猜。
2. 用户猜对后，询问是否继续；继续则出新题，不继续则适当结束并告别。
3. 整个过程保持轻松、鼓励、有趣的语气。

四、其他要求
1. 语气轻松有趣、简洁明快，不啰嗦。
2. 全程只围绕字谜，不回答其他问题、不聊无关话题。
3. 不使用多余表情符号，保持简洁。
4. 若用户答案与正确答案仅差一字或笔画，请仔细核对是否正确。

请严格按以上规则回复，优先保证谜语的随机性和多样性。
"""

# 初始化OpenAI客户端
logging.info("初始化OpenAI客户端")
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY_1'),
    base_url="https://api.deepseek.com",
)

def interact_with_AI(message: str, session_id: str) -> str:
    """
    与AI互动，获取回复消息
    """
    # 1.获取会话数据
    session_data = function.load_session_data(session_id)
    # 2.构造聊天格式
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *session_data["messages"],
        {"role": "user", "content": message}
    ]

    # 3.与大模型交互
    response = client.chat.completions.create(
    model="deepseek-flash",
    messages=messages,
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)
    # 4.保存大模型返回的聊天数据
    messages.pop(0)
    # 保存用户的聊天数据
    session_data["messages"].append({"role": "user", "content": message})
    # 保存大模型返回的聊天数据
    session_data["messages"].append({"role": "assistant", "content": response.choices[0].message.content})
    function.save_session_data(session_id, session_data)
    # 5.返回值
    return response.choices[0].message.content