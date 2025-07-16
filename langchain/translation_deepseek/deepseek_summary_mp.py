from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain, create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, FewShotPromptTemplate
from langchain_experimental.tabular_synthetic_data.openai import create_openai_data_generator
from langchain_experimental.tabular_synthetic_data.prompts import SYNTHETIC_FEW_SHOT_PREFIX, SYNTHETIC_FEW_SHOT_SUFFIX
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from langchain_text_splitters import CharacterTextSplitter
from pydantic import BaseModel
from pydantic.v1 import Field, ConfigDict
from transformers.masking_utils import chunked_overlay

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
    temperature=1.3
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

# 第二种:MapReduce
model_name = "BAAI/bge-large-zh-v1.5"
model_kwargs = {"device": "cpu"}  # 使用GPU加速
encode_kwargs = {"normalize_embeddings": True}

embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=1100, chunk_overlap=0)
split_doc =text_splitter.split_documents(docs)

# 第一步: map阶段
map_template ="""以下是一组文栏documents {docs}
根据这个文档列表，请给出总结摘要:
"""


map_prompt = PromptTemplate.from_template(map_template)
map_llm_chain = map_prompt | deepseek


#第二步:reduce阶段:(combie和 最终的reduce)
reduce_template ="""
以下是组总结摘要:
{docs}
将这些内容提炼成一个最终的、统一的总结摘要:
"""
reduce_prompt = PromptTemplate.from_template(reduce_template)
parser = JsonOutputParser()

# reduce_llm_chain = reduce_prompt | deepseek

"""
reduce的思路:
如果map之后文档的累积token数超过了4000个,那么我们将递归地将文档以<=4000 个token的批次传递给我们的StuffDocumentsChain
一旦这些批量摘要的累积大小小于 4000个token，我们将它们全部传递给 StuffDocumentsChain 以创建最终摘要
"""

#定义一个combine的chain
combine_documents_chain =create_stuff_documents_chain(llm=deepseek, prompt=reduce_prompt, output_parser=parser, document_variable_name='docs')
# combine_documents_chain = StuffDocumentsChain(
#     llm_chain=reduce_llm_chain, document_variable_name="docs"
# )

reduce_documents_chain =ReduceDocumentsChain(
    combine_documents_chain=combine_documents_chain,
    collapse_documents_chain=combine_documents_chain,
    token_max=4000

)

# 合并所有链
map_reduce_chain =MapReduceDocumentsChain(
    llm_chain=map_llm_chain,
    reduce_documents_chain=reduce_documents_chain ,
    document_variable_name='docs',
    return_intermediate_steps=False
)

#第五步:调用最终的链
result = map_reduce_chain.invoke(split_doc)
print(result['output_text'])









