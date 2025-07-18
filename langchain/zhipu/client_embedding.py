from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv
from langchain_community.embeddings import ModelScopeEmbeddings
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
)
from langchain.chains import LLMChain

# 加载环境变量
load_dotenv()

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4-0520",
    openai_api_key=os.getenv("ZHIPU_API_KEY"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
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


# https://www.modelscope.cn/models/iic/nlp_gte_sentence-embedding_chinese-large/summary
embedding = ModelScopeEmbeddings(model_id="iic/nlp_gte_sentence-embedding_chinese-large")


# embedding = HuggingFaceEmbeddings(model_name="iic/nlp_gte_sentence-embedding_chinese-large")

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

chain = {'question': RunnablePassthrough(), 'context': retriever} | prompt_temp | llm

response = chain.invoke('请谈下关于猫的事情')

print(response.content)