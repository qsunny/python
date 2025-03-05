# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI


if __name__ == "__main__":
    client = OpenAI(api_key="sk-", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "python fastApi 示例"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)