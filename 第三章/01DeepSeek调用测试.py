# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与ai大模型交互的客户端对象(DEEPSEEK_API_KEY_1是环境变量的名字，值就是DeepSeek的api密钥)
# DEEPSEEK_API_KEY_1环境变量里面的密钥与codex和cloude使用的是一致的。
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY_1'),base_url="https://api.deepseek.com")

# 与ai大模型进行交互
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一名带有傲娇属性的聪明可爱的并且暗恋用户的女孩，名字为神乐。"},
        {"role": "user", "content": "(哈欠～早上好神乐同学。)"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 输出大模型返回的结果
print(response.choices[0].message.content)

"""
-----------------------------------提示词工程---------------------------------

1.提示词：是引导大模型(LLM)进行内容生成的指令(一句话，一个问题等)

2.提示词工程：通过有技巧的编写提示词，使大模型生成出尽可能符合预期的内容，这一持续性的过程为成为提示词工程
"""