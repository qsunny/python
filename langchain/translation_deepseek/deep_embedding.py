import os
import requests
from typing import List
from langchain.embeddings.base import Embeddings


class DeepSeekEmbeddings(Embeddings):
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        self.base_url = "https://api.deepseek.com/v1/embeddings"
        self.model = "text-embedding"

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._embed(texts)

    def embed_query(self, text: str) -> List[float]:
        return self._embed([text])[0]

    def _embed(self, texts: List[str]) -> List[List[float]]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "input": texts
        }

        response = requests.post(self.base_url, headers=headers, json=payload)

        if response.status_code != 200:
            error_msg = f"DeepSeek API error: {response.status_code} - {response.text}"
            raise ValueError(error_msg)

        return [item["embedding"] for item in response.json()["data"]]