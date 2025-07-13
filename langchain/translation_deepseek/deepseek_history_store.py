import uvicorn
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from dotenv import load_dotenv
import os

from langserve import add_routes
from sympy import content

# 加载环境变量
load_dotenv()

# 初始化 DeepSeek 客户端
"""
https://api-docs.deepseek.com/zh-cn/quick_start/parameter_settings
按使用场景设置 temperature
代码生成/数学解题   	0.0
数据抽取/分析	1.0
通用对话	1.3
翻译	1.3
创意类写作/诗歌创作	1.5
"""
# deepseek = ChatOpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com/v1",  # DeepSeek API 入口
#     model="deepseek-chat",                   # 使用 DeepSeek 官方模型
#     temperature=1.3,                         # 控制创意度 (0-1)
# )

# 初始化ChatOpenAI模型
deepseek = ChatOpenAI(
    model="anthropic/claude-3.7-sonnet",  # 可以在OpenRouter模型列表中选择
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.5,
    max_tokens=1024
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', '你是一个乐于助人的助手。用{language}尽你所能回答所有问题。'),
        MessagesPlaceholder(variable_name="my_message")
    ])

# 创建组装链
chain = prompt_template | deepseek

# 保存记录
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id]= ChatMessageHistory()
    return store[session_id]

do_message = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key= 'my_message'
)

config = {
    'configurable': {
        'session_id': 'zs123'
    }
}

# 第一轮
resp1 = do_message.invoke(
    {
        "my_message": [HumanMessage(content='你好呀，我是Aaron')],
        "language": "中文"
    },
    config = config
)

print(resp1.content)

# 第二轮
resp2 = do_message.invoke(
    {
        "my_message": [HumanMessage(content='请问我的名字叫什么?')],
        "language": "中文"
    },
    config = config
)

print(resp2.content)

# 第三轮 返回流式数据
for resp in do_message.stream({"my_message": [HumanMessage(content='我想让你给我讲个关于唐代诗人李白成长的故事?')], "language": "中文"}, config = config):
    print(resp.content, end='')



# if __name__ == "__main__":

