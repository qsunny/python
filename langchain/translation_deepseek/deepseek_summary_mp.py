from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter  # 更可靠的分割器

# 首先设置所有环境变量
os.environ["USER_AGENT"] = "LangChainSummaryBot/1.0 (contact@example.com)"  # 在加载器前设置
# os.environ['http_proxy'] = 'http://127.0.0.1:10809'  # 按需启用
# os.environ['https_proxy'] = 'http://127.0.0.1:10809'

# 加载环境变量
load_dotenv()

# 初始化DeepSeek
deepseek = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
    model="deepseek-chat",
    temperature=0.3,  # 摘要任务适合较低温度
    max_tokens=2048
)

print("开始加载文档...")
# 加载文档 - 设置明确的用户代理
loader = WebBaseLoader(
    'https://lilianweng.github.io/posts/2023-06-23-agent/',
    header_template={"User-Agent": os.environ["USER_AGENT"]}
)
docs = loader.load()
print(f"已加载文档，包含 {len(docs)} 个文档")

# 使用更可靠的分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,  # 减小分块大小
    chunk_overlap=150,  # 增加重叠保证上下文连贯
    length_function=len,
    is_separator_regex=False
)
split_docs = text_splitter.split_documents(docs)
print(f"文档分割为 {len(split_docs)} 个分块")

# 定义map和reduce提示模板
map_template = """请为以下文本片段生成简洁摘要（不超过3句话）:
{text}

摘要:"""
map_prompt = PromptTemplate.from_template(map_template)

reduce_template = """请将以下多个摘要整合成一个连贯、全面的完整摘要（不超过10句话）:
{text}

完整摘要:"""
reduce_prompt = PromptTemplate.from_template(reduce_template)

# 创建摘要链
chain = load_summarize_chain(
    llm=deepseek,
    chain_type="map_reduce",
    map_prompt=map_prompt,
    combine_prompt=reduce_prompt,
    verbose=False  # 设为True可查看详细过程
)

print("开始生成摘要...")
# 执行摘要
result = chain.invoke({"input_documents": split_docs})
print("\n===== 最终摘要 =====")
print(result["output_text"])