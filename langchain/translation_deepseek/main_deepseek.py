import uvicorn
from fastapi import FastAPI
from langchain.agents.chat.prompt import HUMAN_MESSAGE
from langchain.chains.summarize.map_reduce_prompt import prompt_template
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from langserve import add_routes

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
deepseek = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",  # DeepSeek API 入口
    model="deepseek-chat",                   # 使用 DeepSeek 官方模型
    temperature=1.3,                         # 控制创意度 (0-1)
)

# deepseek = init_chat_model("deepseek-chat", model_provider="deepseek")


# msg = [
#     SystemMessage("请将以下的内容翻译成意大利语"),
#     HumanMessage("你好，请问你要去哪里?")
# ]

# 执行对话
# response = deepseek.invoke(msg)
# print(response)
# print(response.content)

parser = StrOutputParser()
# print(parser.invoke(response))

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', '请将下面的内容翻译成{language}'),
        ('user', '{text}'),
    ])

# 创建组装链
chain = prompt_template | deepseek | parser

# 通过链调用
# print(chain.invoke(msg))
print(chain.invoke({'language': 'english', 'text': '小明期末的英语考试不及格'}))

app = FastAPI(title="langchain第一个语言翻译服务", version="v1.0.0", description="使用langchain翻译任何语言")

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)