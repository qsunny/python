import asyncio
import os
from erniebot_agent.agents import FunctionAgent
from erniebot_agent.chat_models import ERNIEBot
from erniebot_agent.tools import RemoteToolkit

async def main():

    os.environ = {"EB_AGENT_ACCESS_TOKEN": "",
                  "EB_AGENT_LOGGING_LEVEL": "info"}

    llm = ERNIEBot(model="ernie-3.5")  # 初始化大语言模型
    tts_tool = RemoteToolkit.from_aistudio("texttospeech").get_tools()  # 获取语音合成工具
    agent = FunctionAgent(llm=llm, tools=tts_tool)  # 创建智能体，集成语言模型与工具

    # 与智能体进行通用对话
    # result = await agent.run("你好，请自我介绍一下")
    # print(result.text)
    # 模型返回类似如下结果：
    # 你好，我叫文心一言，是百度研发的知识增强大语言模型，能够与人对话互动，回答问题，协助创作，高效便捷地帮助人们获取信息、知识和灵感。

    # 请求智能体根据输入文本，自动调用语音合成工具
    # result = await agent.run("把上一轮的自我介绍转成语音")
    # print(result.text)

    result = await agent.run("使用python flash写个web的示例")
    print(result.text)
    # 模型返回类似如下结果：
    # 根据你的请求，我已经将自我介绍转换为语音文件，文件名为file-local-c70878b4-a3f6-11ee-95d0-506b4b225bd6。
    # 你可以使用任何支持播放音频文件的设备或软件来播放这个文件。如果你需要进一步操作或有其他问题，请随时告诉我。

    # 将智能体输出的音频文件写入test.wav, 可以尝试播放
    # audio_file = result.steps[-1].output_files[0]
    # await audio_file.write_contents_to("./test.wav")

asyncio.run(main())