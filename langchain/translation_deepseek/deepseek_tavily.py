from webbrowser import Chrome

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings, OpenAI
from langchain_tavily.tavily_search import TavilySearch
from dotenv import load_dotenv
import os

from langgraph.prebuilt import chat_agent_executor

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

# response = deepseek.invoke([HumanMessage(content='今天深圳天气怎么样？')])
# print(response.content)


# Langchain内置了一个工具，可以轻松地使用Tavily搜索引擎作为工具
search = TavilySearch(max_results=2)
# print(search.invoke("今天深圳天气怎么样？"))

# 模型绑定工具
tools = [search]
# model_with_tools = deepseek.bind_tools(tools)

# 模型可以自动推理:是否需要调用工具去完成用户的案
# resp = model_with_tools.invoke([HumanMessage(content='今天深圳天气怎么样？')])

# print(f'Model_Result_Content: {resp.content}')
# print(f'Tools_Result_Content: {resp.tool_calls}')
#
# resp2 = model_with_tools.invoke([HumanMessage(content='中国有十三朝古都之称是那个城市？')])
#
# print(f'Model_Result_Content: {resp2.content}')
# print(f'Tools_Result_Content: {resp2.tool_calls}')

# 创建代理
agent_executor = chat_agent_executor.create_tool_calling_executor(deepseek, tools)

resp = agent_executor.invoke({"messages": [HumanMessage(content='今天深圳天气怎么样？')]})
print(resp["messages"])
print(resp["messages"][2].content)


resp2 = agent_executor.invoke({"messages": [HumanMessage(content='中国有十三朝古都之称是那个城市？')]})
print(resp2["messages"])

# if __name__ == "__main__":
