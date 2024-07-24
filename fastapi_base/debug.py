# -*- coding: utf-8 -*-
"""
Created on 2023-03-23 16:06
---------
@summary: 爬虫入口
---------
@author: pepsi
"""
from core.server import InitializeApp
import uvicorn

app = InitializeApp()
if __name__ == "__main__":
    uvicorn.run(
        app='debug:app',
        host="0.0.0.0",
        port=4396,
        reload=True,
    )
