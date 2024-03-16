import requests


if __name__ == "__main__":
    print("=========")

    resp = requests.get('http://127.0.0.1:8000/').text
    print(resp)

    resp = requests.get('http://127.0.0.1:8000/info').text
    print(resp)