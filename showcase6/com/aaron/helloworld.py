# -*- coding: utf-8 -*-
"""枚举"""
__author__="Aaron.qiu"

import wx

if __name__=="__main__":
    app = wx.App()
    window = wx.Frame(None, title="wxPython - www.yiibai.com", size=(400, 300))
    panel = wx.Panel(window)
    label = wx.StaticText(panel, label="Hello World", pos=(100, 100))
    window.Show(True)
    app.MainLoop()




