from langchain.chains.combine_documents.stuff import StuffDocumentsChain, create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, FewShotPromptTemplate
from langchain_experimental.tabular_synthetic_data.openai import create_openai_data_generator
from langchain_experimental.tabular_synthetic_data.prompts import SYNTHETIC_FEW_SHOT_PREFIX, SYNTHETIC_FEW_SHOT_SUFFIX

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from pydantic import BaseModel
from pydantic.v1 import Field, ConfigDict

# os.environ['http_proxy']= 'socks5://127.0.0.1:10808'
# os.environ['https_proxy']= 'socks5://127.0.0.1:10808'

os.environ['http_proxy']= 'http://127.0.0.1:10809'
os.environ['https_proxy']= 'http://127.0.0.1:10809'

os.environ["USER_AGENT"] = "MyApp/1.0 (support@example.com)"
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
    model_kwargs={
        "response_format": {"type": "json_object"}  # 必须设置的响应格式
    },
)

# 初始化ChatOpenAI模型
# deepseek = ChatOpenAI(
#     model="anthropic/claude-3.7-sonnet",  # 可以在OpenRouter模型列表中选择
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
#     temperature=0.5,
#     max_tokens=1024
# )

# 加载我们的文档。我们将使用 WebBaseLoad
loader = WebBaseLoader('https://lilianweng.github.io/posts/2023-06-23-agent/')
docs = loader.load()

# 第一种:Stuff

# chain = load_summarize_chain(deepseek, chain_type='stuff')
# result = chain.invoke(docs)
# print(result['output_text'])

# Stuff的第二种写法# 定义提示
prompt_template = """
针对下面的内容，写一个简洁的总结摘要:
{context}

要求:
- 语言简洁明了，中文输出
- 不超过150字
- 突出核心技术点

简洁的总结摘要:
"""

prompt = PromptTemplate.from_template(prompt_template)

# llm_chain = prompt | deepseek
# stuff_chain = create_stuff_documents_chain(llm=deepseek, prompt=prompt, document_variable_name='text')

# 创建文档链 - 使用LangChain推荐方式
try:
    stuff_chain = create_stuff_documents_chain(llm=deepseek, prompt=prompt)
    input_data = {
        "context": docs,  # 必须是文档列表
    }

    # 安全调用链
    result = stuff_chain.invoke(input_data)
    print("✅ 成功生成的摘要:")
    print(result)  # create_stuff_documents_chain直接返回字符串
except Exception as e:
    print(f"❌ 发生错误: {str(e)}")









