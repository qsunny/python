from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
import warnings

# 1. 首先设置所有环境变量
os.environ["USER_AGENT"] = "LangChainSummaryBot/1.0 (contact@example.com)"
# os.environ['http_proxy'] = 'http://127.0.0.1:10809'
# os.environ['https_proxy'] = 'http://127.0.0.1:10809'

# 2. 忽略特定警告
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_openai.*")

# 加载环境变量
load_dotenv()

# 3. 初始化DeepSeek - 添加超时参数
deepseek = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
    model="deepseek-chat",
    temperature=0.3,
    max_tokens=2048,
    request_timeout=60  # 增加超时时间
)

print("开始加载文档...")
# 4. 加载文档 - 直接传递用户代理头
headers = {"User-Agent": os.environ["USER_AGENT"]}
loader = WebBaseLoader(
    web_path='https://lilianweng.github.io/posts/2023-06-23-agent/',
    header_template=headers
)
docs = loader.load()
print(f"已加载文档，包含 {len(docs)} 个文档")

# 5. 使用更可靠的分割器并处理分块大小问题
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150,
    length_function=len,
    add_start_index=True  # 添加起始索引
)
split_docs = text_splitter.split_documents(docs)
print(f"文档分割为 {len(split_docs)} 个分块")

# 6. 检查并调整过大分块
for i, doc in enumerate(split_docs):
    if len(doc.page_content) > 1000:
        print(f"警告: 分块 {i} 大小为 {len(doc.page_content)} 字符")
        # 自动分割过大的分块
        if len(doc.page_content) > 1500:
            new_chunks = text_splitter.split_text(doc.page_content)
            print(f"  分块 {i} 被分割为 {len(new_chunks)} 个小分块")
            # 在实际应用中，这里需要替换原始分块

# 7. 定义优化的提示模板
map_template = """请为以下文本片段生成简洁摘要（2-3句话）:
{text}

摘要:"""
map_prompt = PromptTemplate.from_template(map_template)

reduce_template = """请将以下多个摘要整合成一个连贯、全面的完整摘要:
{text}

完整摘要:"""
reduce_prompt = PromptTemplate.from_template(reduce_template)

# 8. 创建摘要链 - 使用更可靠的map_reduce实现
chain = load_summarize_chain(
    llm=deepseek,
    chain_type="map_reduce",
    map_prompt=map_prompt,
    combine_prompt=reduce_prompt,
    verbose=True  # 开启详细输出以调试
)

print("开始生成摘要...")
try:
    # 9. 执行摘要 - 确保正确输入格式
    result = chain.invoke({"input_documents": split_docs})

    print("\n===== 最终摘要 =====")
    print(result["output_text"])

    # 10. 显示token使用情况（如果可用）
    if 'token_usage' in result:
        usage = result['token_usage']
        print(
            f"\nToken使用情况: 输入={usage.get('prompt_tokens', 'N/A')}, 输出={usage.get('completion_tokens', 'N/A')}")
    else:
        print("\nToken使用信息不可用")

except Exception as e:
    print(f"摘要生成失败: {str(e)}")
    print("尝试简化处理...")

    # 备选方案：仅处理前几个分块
    try:
        result = chain.invoke({"input_documents": split_docs[:5]})
        print("\n===== 部分摘要 =====")
        print(result["output_text"])
    except Exception as e2:
        print(f"备选方案也失败: {str(e2)}")