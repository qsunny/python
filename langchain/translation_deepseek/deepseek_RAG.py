from webbrowser import Chrome

import bs4
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.chat_message_histories import ChatMessageHistory

from dotenv import load_dotenv
import os

# os.environ['http_proxy']= '127.0.0.1:10808'
# os.environ['https_proxy']= '127.0.0.1:10808'
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

# 加载数据 从网页
loader = WebBaseLoader(
    web_paths=['https://lilianweng.github.io/posts/2023-06-23-agent/'],
    bs_kwargs=dict(
        parse_only = bs4.SoupStrainer(class_ = ('post-title','post-meta','post-header','post-content'))
    )
)

docs = loader.load()

# print(len(docs))
# print(docs)

# text = "Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver."

# 文本切割
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# res = splitter.split_text(text)
# for sw in res:
#     print(sw, end="***\n")

splits = splitter.split_documents(docs)

model_name = "BAAI/bge-large-zh-v1.5"
model_kwargs = {"device": "cpu"}  # 使用GPU加速
encode_kwargs = {"normalize_embeddings": True}

embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# 存储
vectorstore = Chroma.from_documents(documents=splits, embedding=embedding, persist_directory="./chroma_db2")

# 检索器
retriever = vectorstore.as_retriever()

#创建一个问题的模板
system_prompt ="""You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, say that you don't know, 
Use three sentences maximum and keep the answer concise. \n

{context}
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)

# 创建chain
chain1 = create_stuff_documents_chain(deepseek, prompt)
# chain2 = create_retrieval_chain(retriever, chain1)
#
# resp = chain2.invoke({'input':"What is Task Decomposition?"})
#
# print(resp['answer'])

"""
一般情况下，我们构建的链(chain)直接使用输入问答记录来关联上下文。但在此案例中，查询检索器直接使用输也需要对话上下文才能被理解
解决办法:
问题。这可以被简单地认添加一个子链(chain)，它采用最新用户问题和聊天历史，并在它引用历史信息中的任何信息时重新表述问题 这可以被简单地认为是构建一个新的“历史感知"检索器。
这个子链的目的:让检索过程融入了对话的上下文
"""
# 创建一个子链
# 子链提示模板
contextualize_q_system_prompt ="""Given a chat history and the latest user question
which might reference context in the chat history,formulate a standalone question which can be understood without the chat history. Do NOT answer the question,
just reformulate it if needed and otherwise return it as is.
"""

retriever_history_temp = ChatPromptTemplate.from_messages(
    [
        ('system',contextualize_q_system_prompt),
        MessagesPlaceholder('chat_history'),
        ("human", "{input}")
    ]
)

#创建一个子链
history_chain = create_history_aware_retriever(deepseek, retriever, retriever_history_temp)

# 保存问答历史记录
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id]= ChatMessageHistory()
    return store[session_id]

# 创建父链 chain
chain = create_retrieval_chain(history_chain, chain1)

result_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

# 第一轮对话
resp1 = result_chain.invoke(
    {'input': 'What is Task Decomposition?'},
    config={'configurable': {'session_id':'zs123456'}}
)

print(resp1['answer'])

# 第二轮对话
resp2 = result_chain.invoke(
    {'input': 'What are common ways of doing it?'},
    config={'configurable': {'session_id':'zs123456'}}
)

print(resp2['answer'])

# if __name__ == "__main__":
