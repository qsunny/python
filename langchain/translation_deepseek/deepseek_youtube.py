import datetime

import uvicorn
from langchain_chroma import Chroma
from langchain_community.document_loaders import YoutubeLoader
from pytube import YouTube
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import requests
from langchain_text_splitters import RecursiveCharacterTextSplitter

# os.environ['http_proxy']= 'socks5://127.0.0.1:10808'
# os.environ['https_proxy']= 'socks5://127.0.0.1:10808'

os.environ['http_proxy']= 'http://127.0.0.1:10809'
os.environ['https_proxy']= 'http://127.0.0.1:10809'

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
)

# 初始化ChatOpenAI模型
# deepseek = ChatOpenAI(
#     model="anthropic/claude-3.7-sonnet",  # 可以在OpenRouter模型列表中选择
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1",
#     temperature=0.5,
#     max_tokens=1024
# )

urls =[
    "https://www.youtube.com/watch?v=HAn9vnJy6S4",
    "https://www.youtube.com/watch?v=hvAPnpSfSGo",
    "https://www.youtube.com/watch?v=HAnw168huqA",
    "https://www.youtube.com/watch?v=d0yGdNEWdn0&t=8s",
    "https://www.youtube.com/watch?v=T-D1OfcDW1M&t=18s",
    "https://www.youtube.com/watch?v=sVcwVQRHIc8",
    "https://www.youtube.com/watch?v=2IK3DFHRFfw",
    "https://www.youtube.com/watch?v=I64RtGofPW8"
    ]


import yt_dlp as youtube_dl
import random

# 代理列表（需要自行添加有效代理）
proxy_list = [
    'http://127.0.0.1:10809'
]

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'noplaylist': True,
    'proxy': random.choice(proxy_list),
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.youtube.com/',
    }
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info("https://www.youtube.com/watch?v=I64RtGofPW8", download=False)
    print(info)

# document的数组
docs =[]
for url in urls:
    # 一个Youtube的视频对应一个document
    print(url)
    # docs.extend(YoutubeLoader.from_youtube_url(url, add_video_info=True, language="en").load())
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    docs.extend(yt.streams.all())
print(len(docs))




# 给doc添加额外的元数据:视频发布的年份
for doc in docs:
    doc.metadata['publish_year'] = int(datetime.datetime.strptime(doc.metadata['publish_date'], '%Y-%m-%d %H:%M:%S').strftime('%Y'))

print(docs[0].metadata)
#第一个视频的字母内容
print(docs[0].page_content[:500])

# 根据多个doc构建向量数据库
text_splitter =RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=30)
split_doc =text_splitter.split_documents(docs)

# BAAI/bge-m3 支持多语言混合检索，稀疏+密集双模式，适合高精度RAG系统
# BAAI/bge-reranker-v2-m3 问题 答案 相关度
model_name = "BAAI/bge-large-zh-v1.5"
model_kwargs = {"device": "cpu"}  # 使用GPU加速
encode_kwargs = {"normalize_embeddings": True}

embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

persist_dir ='./chroma_youtube_db'
# 向量数据库
vector_store = Chroma.from_documents(split_doc, embedding=embedding, persist_directory=persist_dir)

# if __name__ == "__main__":

