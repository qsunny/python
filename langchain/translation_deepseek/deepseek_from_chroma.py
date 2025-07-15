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


# BAAI/bge-m3 支持多语言混合检索，稀疏+密集双模式，适合高精度RAG系统
# BAAI/bge-reranker-v2-m3 问题 答案 相关度
model_name = "BAAI/bge-large-zh-v1.5"
model_kwargs = {"device": "cpu"}  # 使用GPU加速
encode_kwargs = {"normalize_embeddings": True}

embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

persist_dir ='./chroma_youtube_db'
# 向量数据库
vector_store = Chroma(embedding_function=embedding, persist_directory=persist_dir)
result = vector_store.similarity_search_with_score('how do I build a RAG agent?')
print(result[0])
# if __name__ == "__main__":

system ="""You are an expert at coverting user questions into database query
You have access to a database of  tutorial videos about a software library for
Given a question,return a list of database queries optimized to retrieve the

If there are acronyms or words you are not familiar with, do not try to rephrahe
"""
prompt = ChatPromptTemplate.from_mesages(
    [
        ("system", system)
        ("human", "{question}"),
    ]
)

# pydantic
class Search(BaseModel):
    # 内容的相似性和发布年份
    query: str = Field( None, description = 'Similarity search query applied to yideo transcripts.')
    publish_year:Optional[int] = Field( None, description = 'Year video was published.')



chain ={'question':RunnablePassthrough()} | prompt | deepseek.with_structured_output(schema=Search)

resp = chain.invoke('how do I build a RAG agent?')
print(resp)


def retrieval(search:Search)-> List[Document]:

    # 根据publish_year，存在得到一个检索条件
    if search.publish_year:
        #"$eq"是Chroma向量数据库的固定语法
        _filter = {'publish_year': {"$eq": search.publish_year}}

    return vector_store.similarity_search(search.guery, filter=_filter)

new_chain =chain| retrieval

result = new_chain.invoke('videos on RAG published in 2023')

print([(doc.metadata['title'], doc.metadata['publish_year']) for doc in result])










