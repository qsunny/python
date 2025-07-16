from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os


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

import getpass
import os

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model

llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

from langchain_core.documents import Document

documents = [
    Document(page_content="Apples are red", metadata={"title": "apple_book"}),
    Document(page_content="Blueberries are blue", metadata={"title": "blueberry_book"}),
    Document(page_content="Bananas are yelow", metadata={"title": "banana_book"}),
]



# Map
map_template = "Write a concise summary of the following: {docs}."
map_prompt = ChatPromptTemplate([("human", map_template)])
# map_chain = LLMChain(llm=llm, prompt=map_prompt)
map_chain = map_prompt | llm


# Reduce
reduce_template = """
The following is a set of summaries:
{docs}
Take these and distill it into a final, consolidated summary
of the main themes.
"""
reduce_prompt = ChatPromptTemplate([("human", reduce_template)])
# reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)
reduce_chain = reduce_prompt | llm


# Takes a list of documents, combines them into a single string, and passes this to an LLMChain
combine_documents_chain = StuffDocumentsChain(
    llm_chain=reduce_chain, document_variable_name="docs"
)
# combine_documents_chain =create_stuff_documents_chain(llm=reduce_llm_chain, prompt=reduce_prompt, output_parser=parser, document_variable_name='docs')

# Combines and iteratively reduces the mapped documents
reduce_documents_chain = ReduceDocumentsChain(
    # This is final chain that is called.
    combine_documents_chain=combine_documents_chain,
    # If documents exceed context for `StuffDocumentsChain`
    collapse_documents_chain=combine_documents_chain,
    # The maximum number of tokens to group documents into.
    token_max=1000,
)

# Combining documents by mapping a chain over them, then combining results
map_reduce_chain = MapReduceDocumentsChain(
    # Map chain
    llm_chain=map_chain,
    # Reduce chain
    reduce_documents_chain=reduce_documents_chain,
    # The variable name in the llm_chain to put the documents in
    document_variable_name="docs",
    # Return the results of the map steps in the output
    return_intermediate_steps=False,
)


result = map_reduce_chain.invoke(documents)

print(result["output_text"])





