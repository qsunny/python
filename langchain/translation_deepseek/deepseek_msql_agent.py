from operator import itemgetter

import uvicorn
from langchain_community.agent_toolkits import SQLDatabaseToolkit

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from langgraph.prebuilt import chat_agent_executor

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

# sqlalchemy
HOSTNAME ='172.27.93.236'
PORT ='3306'
DATABASE ='water'
USERNAME = 'root'
PASSWORD ='root'
# mysqlclient驱动URL
MYSQL_URI ='mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

db = SQLDatabase.from_uri(MYSQL_URI)


# 创建工具
toolkit = SQLDatabaseToolkit(db=db, llm=deepseek)
tools = toolkit.get_tools()
# 使用agent完整整个数据库的整合
system_prompt ="""
您是一个被设计用来与S0L数据库交互的代理。
给定一个输入问题，创建一个语法正确的SQL语句并执行，然后查看查询结果并返回答案。
除非用户指定了他们想要获得的示例的具体数量，否则始终将SQL查询限制为最多10个结果。
你可以按相关列对结果进行排序，以返回MySQL数据库中最匹配的数据。
您可以使用与数据库交互的工具。在执行査询之前，你必须仔细检査。如果在执行査询时出现错误，请重写査询SQL并重试。
不要对数据库做任何DML语句(插入，更新，删除，删除等)。

首先，你应该查看数据库中的表，看看可以查询什么。
不要跳过这一步。
然后查询最相关的表的模式。
"""
system_message =SystemMessage(content=system_prompt)

# 创建代理
agent_executor = chat_agent_executor.create_tool_calling_executor(deepseek, tools, prompt=system_message)

# resp = agent_executor.invoke({'messages': [HumanMessage(content='请问用户元亨利贞在2024年4月份下了多少订单?')]})
resp = agent_executor.invoke({'messages': [HumanMessage(content='请问都有那些部门,每个部门都有多少人, 那个部门的人数是最多的?')]})

result =resp['messages']
print(result)
print(len(result))
#最后一个才是真正的答案
print(result[len(result)-1])
# if __name__ == "__main__":

