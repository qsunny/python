# 项目名称：数据分析小助手
# 功能：实现数据清洗、分析和可视化
# 运行环境：Python 3.8+、pandas、matplotlib
# 安装步骤：pip install -r requirements.txt
# 运行方法：python main.py
# 测试报告位置：test/test_report.html


# 模块：data_cleaning
# 功能：对原始数据进行清洗，包括去除重复值、处理缺失值、异常值检测等
# 类：DataCleaner
# 方法：
#   __init__(data)：初始化，传入原始数据
#   remove_duplicates()：去除重复值
#   handle_missing_values(strategy)：处理缺失值，strategy 可选"删除"、"均值填充"、"中位数填充"等
#   detect_outliers(method)：异常值检测，method 可选"Z-Score"、"IQR"等

# 部署步骤：
# 1. 在服务器上创建项目目录：mkdir /data/analytics_project
# 2. 将代码拷贝到服务器：scp -r * username@server:/data/analytics_project
# 3. 安装项目依赖：cd /data/analytics_project && pip install -r requirements.txt
# 启动方法：python /data/analytics_project/main.py --env production
# 停止方法：通过任务管理器或进程 ID 停止 python 进程