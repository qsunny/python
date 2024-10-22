import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("Canvas 中文字体设置示例")

# 创建一个Canvas
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# 指定一个支持中文的字体（例如：'SimHei'（黑体），确保字体名称在系统中存在）
# 注意：字体名称可能因操作系统而异
chinese_font = ("SimHei", 16)  # 字体名称和大小

# 在Canvas上绘制中文文本
canvas.create_text(200, 100, text="你好，世界！", fill="black", font=chinese_font)

# 运行主循环
root.mainloop()