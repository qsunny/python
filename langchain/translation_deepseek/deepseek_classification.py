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

# 1、定义数据模型
class Classification(BaseModel):
    """
        文本分类数据模型（兼容 OpenAI JSON Schema）
        """
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{"sentiment": "negative", "aggressiveness": 7, "language": "zh"}]
        }
    )

    sentiment: str = Field(
        default="neutral",
        json_schema={
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "文本情感分类结果"
        }
    )

    aggressiveness: int = Field(
        default=1,
        json_schema={
            "type": "integer",
            "minimum": 0,
            "maximum": 10,
            "description": "攻击性程度评分（0-10分）"
        }
    )

    language: str = Field(
        default="zh",
        json_schema={
            "type": "string",
            "pattern": "^[a-z]{2}$",
            "description": "文本语言代码（ISO 639-1）"
        }
    )


# 创建一个用于提取信息的提示模板
tagging_prompt = ChatPromptTemplate.from_template(
    """
    请严格按以下JSON格式分析文本：
    {{
      "sentiment": "<情感分类>",
      "aggressiveness": <攻击性评分>,
      "language": "<语言代码>"
    }}
    
    文本分析要求：
    1. 情感分类只允许使用: ["positive", "negative", "neutral"]
    2. 攻击性评分范围: 0-10整数（0=无害，10=高度攻击性）
    3. 语言代码使用ISO 639-1标准（如中文=zh，英文=en）
    
    待分析文本:
    {input}
    """
)


# 4. 创建输出解析链
parser = JsonOutputParser(pydantic_object=Classification)

# 5. 构建处理链（标准LangChain流水线）
chain = tagging_prompt | deepseek | parser

# 6. 安全执行函数（含错误处理）
def analyze_text(text: str, max_retry=3):
    for attempt in range(max_retry):
        try:
            return chain.invoke({"input": text})
        except Exception as e:
            if attempt == max_retry-1:
                print(f"⚠️ 最终失败: {str(e)}")
                # 返回保底安全值
                return Classification()
            print(f"⚠️ 尝试 {attempt+1}/{max_retry} 失败，重试中...")

# 7. 执行分析
input_text = "中国人民大学的王教授:师德败坏，做出的事情实在让我生气!"
result = analyze_text(input_text)

print(f"✅ 分析结果: {result}")
