from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, FewShotPromptTemplate
from langchain_experimental.tabular_synthetic_data.openai import create_openai_data_generator
from langchain_experimental.tabular_synthetic_data.prompts import SYNTHETIC_FEW_SHOT_PREFIX, SYNTHETIC_FEW_SHOT_SUFFIX

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from pydantic import BaseModel

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

#生成一些结构化的数据:5个步骤
# 1、定义数据模型
class MedicalBilling(BaseModel):
    patient_id: int
    patient_name: str
    diagnosis_code: str
    procedure_code: str
    total_charge: float
    insurance_claim_amount: float

# 2. 定义提示模板组件（新增！）
SYNTHETIC_FEW_SHOT_PREFIX = """你是一个医疗数据生成器，请根据以下示例生成虚假但格式正确的医疗账单数据："""
SYNTHETIC_FEW_SHOT_SUFFIX = """
现在请生成关于{subject}的虚假医疗账单数据。要求：
1. 使用真实但生僻的中国人名
2. {extrainfo}
请严格按以下JSON格式输出：
{{
    "patient_id": <整数>,
    "patient_name": "<中文姓名>",
    "diagnosis_code": "<疾病代码>",
    "procedure_code": "<治疗代码>",
    "total_charge": <浮点数>,
    "insurance_claim_amount": <浮点数>
}}"""

# 2 提供一些样例数据给AI
examples = [
    {"example": "Patient ID:13456, Patient Name:张娜, diagnosis Code:J20.9, Procedure Code:99203, Total charge:$500, Insurance Claim amount:$1500"},
    {"example": "Patient ID:739012, Patient Name:王兴鹏, diagnosis Code:M54.5, Procedure Code:96541, Total charge:$76.3, Insurance Claim amount:$3500"},
    {"example": "Patient ID:739012, Patient Name:张家辉, diagnosis Code:M64.3, Procedure Code:76511, Total charge:$130, Insurance Claim amount:$1200"}
]

#3、创建一个提示模板，用来指导AI生成符合规定的数据
openai_template = PromptTemplate(input_variables=['example'], template="{example}")

prompt_template = FewShotPromptTemplate(
    prefix=SYNTHETIC_FEW_SHOT_PREFIX,
    suffix=SYNTHETIC_FEW_SHOT_SUFFIX,
    examples=examples,
    example_prompt=openai_template,
    input_variables=['subject','extrainfo']
)

output_parser = JsonOutputParser()
# 4、创建一个结构化数据的生成器
generator = create_openai_data_generator(
    output_schema=MedicalBilling,
    prompt=prompt_template,
    output_parser=output_parser,
    llm=deepseek
)

#5、调用生成器
result = generator.generate(
    subject='医疗账单',
    # extrainfo='名字可以是随机的，最后使用比较生僻的人名。',
    extrainfo='医疗总费用呈现正态分布，最小的总费用为1000',
    runs=10   #指定生成数据的数置
)

print(result)









