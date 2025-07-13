from webbrowser import Chrome

import uvicorn
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory, RunnableLambda, RunnablePassthrough
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI, OpenAIEmbeddings, OpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from dotenv import load_dotenv
from langchain_google_genai import embeddings, GoogleGenerativeAIEmbeddings;
import os
from openai import OpenAI, api_key

from langserve import add_routes
from sympy import content

from deep_embedding import DeepSeekEmbeddings



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


# 准备测试数据，假设我们提供的文档数据如下:
documents= [
    Document(
        page_content="狗是伟大的伴侣，以其忠诚和友好而闻名。",
        metadata={"source":"哺乳动物宠物文档"}
    ),
    Document(page_content="猫是独立的宠物，通常喜欢自己的空间。",
             metadata={"source":"哺乳动物宠物文档"}
    ),
    Document(
        page_content="金鱼是初学者的流行宠物，需要相对简单的护理。",
        metadata={"source":"鱼类宠物文档"}
    ),
    Document(
        page_content="鹦鹉是聪明的鸟类，能够模仿人类的语言。",
        metadata={"source":"鸟类宠物文档"}
    ),
    Document(
        page_content="兔子是社交动物，需要足够的空间跳跃。",
        metadata={"source": "哺乳动物宠物文档"}
    )
]


# embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# embedding = DeepSeekEmbeddings(api_key=os.getenv("DEEPSEEK_API_KEY"))

model_name = "BAAI/bge-large-zh-v1.5"
model_kwargs = {"device": "cpu"}  # 使用GPU加速
encode_kwargs = {"normalize_embeddings": True}

embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# 向量数据库
vector_store = Chroma.from_documents(documents, embedding=embedding, persist_directory="./chroma_db")

# 相似度的查询:返回相似的分数，分数越低相似度越高
# print(vector_store.similarity_search_with_score('咖啡猫'))


# 检索器 .bind(k=1) 返回相似度最高的第一个
retriever = RunnableLambda(vector_store.similarity_search).bind(k=1)

# print(retriever.batch(['咖啡猫','鲨鱼']))

# 提示模板
message = """
使用提供的上下文仅回答这个问题
{question}
上下文
{context}
"""

prompt_temp = ChatPromptTemplate.from_messages([('human', message)])

chain = {'question': RunnablePassthrough(), 'context': retriever} | prompt_temp | deepseek

response = chain.invoke('请谈下关于猫的事情')

print(response.content)
# if __name__ == "__main__":

