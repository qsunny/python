from openai import OpenAI
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from zhipuai import ZhipuAI

# 加载环境变量
load_dotenv()

client = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY")) # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4-0520",  # 填写需要调用的模型编码
    messages=[
        {"role": "user", "content": "当前流行的大模型都有那些，分别从应用领域、优势阐述一下"},
        # {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
        # {"role": "user", "content": "智谱AI开放平台"},
        # {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
        # {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
    ],
)
# print(response.choices[0].message)
print(response.choices[0].message.content)