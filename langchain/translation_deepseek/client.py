from langserve import RemoteRunnable

if __name__ == "__main__":
    client = RemoteRunnable(url="http://localhost:8000/chain/")
    response = client.invoke({"language": "Korean","text": "我的英文成绩很糟糕"})
    print(response)