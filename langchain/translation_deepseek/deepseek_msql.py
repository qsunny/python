from operator import itemgetter

import uvicorn
from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os



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

# print(db.get_usable_table_names())
# print(db.run("SELECT * from t_sys_user limit 100;"))

# 使用模型和数据库结合
test_chain = create_sql_query_chain(deepseek, db)

# resp = test_chain.invoke({"question": "请问用户表有多少条数据?"})

# print(resp)

answer_prompt = PromptTemplate.from_template(
"""给定以下用户问题、可能的SQL语句和SQL执行后的结果，回答用户问题。
Question: {question}
SQL Query: {query}
SQL Result: {result}
回答: """
)

# 创建一个执行sql语句的工具
execute_sql_tool = QuerySQLDatabaseTool(db=db)
# 1、生成SQL，2、执行SQL
# 3 模板 模型
chain =(RunnablePassthrough.assign(query=test_chain).assign(result=itemgetter('query')| execute_sql_tool)
        | answer_prompt
        | deepseek
        | StrOutputParser()
)

resp = chain.invoke(input={"question": "用户元亨利贞在2024年4月份下了多少订单?"})
print(resp)




# if __name__ == "__main__":

