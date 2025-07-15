import datetime
from typing import Optional, List

import uvicorn
from langchain_chroma import Chroma
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from pydantic.v1 import BaseModel, Field
from pytube import YouTube
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import requests
from langchain_text_splitters import RecursiveCharacterTextSplitter

# os.environ['http_proxy']= 'socks5://127.0.0.1:10808'
# os.environ['https_proxy']= 'socks5://127.0.0.1:10808'

os.environ['http_proxy']= 'http://127.0.0.1:10809'
os.environ['https_proxy']= 'http://127.0.0.1:10809'

# 后续请求自动使用代理
# response = requests.get('https://www.youtube.com')
# print(f"当前IP: {response.text}")  # 验证代理生效

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

# 初始化ChatOpenAI模型
# deepseek = ChatOpenAI(
#     model="anthropic/claude-3.7-sonnet",  # 可以在OpenRouter模型列表中选择
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
#     temperature=0.5,
#     max_tokens=1024
# )

# pydantic: 处理数据，验证数据，定义数据的格式，虚拟化和反虚拟化，类型转换等等

#定义一个数据，
class Person(BaseModel):
    """
        关于一个人的数据模型
    """

    name: Optional[str] = Field(default=None, description='表示人的名字')

    hair_color: Optional[str]= Field(default=None, description="如果知道的话，这个人的头发颜色")

    height_in_meters : Optional[str]= Field(default=None, description="以米为单位测量的高度")


class ManyPerson(BaseModel):
    """
    数据模型类:代表多个人
    """

    people : List[Person]


#定义自定义提示以提供指令和任何其他上下文。
#1)你可以在提示模板中添加示例以提高提取质量
#2)引入额外的参数以考虑上下文(例如，包括有关提取文本的文档的元数据。)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个专业的提取算法。"
            "只从未结构化文本中提取相关信息。"
            "如果你不知道要提取的属性的值，"
            "返回该属性的值为null。"
        ),
        #请参阅有关如何使用参考记录消息历史的案例
        #MessagesPlaceholder('examples'),
        ("human","{text}")
    ]
)

# with_structured_output 模型的输出是一个结构化的数据
chain ={'text':RunnablePassthrough()}|prompt | deepseek.with_structured_output(schema=ManyPerson, method="function_calling")
# text = '马路上走来一个女生，长长的黑头发披在肩上，大概1米7左右'
text = '马路上走来一个女生，长长的黑头发披在肩上，大概1米7左右。走在她旁边的是她的男朋友,叫刘海; 一头白银发,比她高10厘米'
resp = chain.invoke(text)
print(resp)