from dotenv import load_dotenv
import os

from langchain_community.tools import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent


# 加载环境变量
load_dotenv()

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4-air-250414",
    openai_api_key=os.getenv("ZHIPU_API_KEY"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)


tools = [TavilySearchResults(max_results=2)]
prompt = hub.pull("hwchase17/react")

# Choose the LLM to use
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
resp = agent_executor.invoke({"input": "what is LangChain?"})

print(resp)