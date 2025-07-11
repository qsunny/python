import pandas as pd
from datetime import datetime, timedelta
import re



# 解析输入文本，提取信息
def extract_data(text):
    data = {}
    # 提取日期和时间
    time_match = re.search(r'(\d{2}:\d{2})～(\d{2}:\d{2})', text)
    if time_match:
        data['开始时间'] = time_match.group(1)
        data['结束时间'] = time_match.group(2)

    # 提取套压
    tya_match = re.search(r'套压(\d+\.\d+)↑(\d+\.\d+)MPa', text)
    if tya_match:
        data['套压'] = f"{tya_match.group(1)}↑{tya_match.group(2)}"

    # 提取排液量
    pyl_match = re.search(r'排液量:(\d+\.\d+)m³', text)
    if pyl_match:
        data['排液量'] = float(pyl_match.group(1))

    # 提取累计排液量
    ljpyl_match = re.search(r'累计排液量(\d+\.\d+)m³', text)
    if ljpyl_match:
        data['累计排液量'] = float(ljpyl_match.group(1))

    # 提取应排液量
    ypyl_match = re.search(r'占应排液(\d+\.\d+)m³的', text)
    if ypyl_match:
        data['应排液量'] = float(ypyl_match.group(1))

    # 提取占比
    zb_match = re.search(r'的(\d+\.\d+)%', text)
    if zb_match:
        data['排液占比'] = float(zb_match.group(1))

    # 提取余液量
    yyl_match = re.search(r'余液量(\d+\.\d+)m³', text)
    if yyl_match:
        data['余液量'] = float(yyl_match.group(1))

    # 提取密度
    md_match = re.search(r'密度(\d+\.\d+)g/cm', text)
    if md_match:
        data['密度'] = float(md_match.group(1))

    # 提取粘度
    nd_match = re.search(r'粘度(\d+)s', text)
    if nd_match:
        data['粘度'] = int(nd_match.group(1))

    # 提取PH值
    ph_match = re.search(r'PH(\d+)', text)
    if ph_match:
        data['PH值'] = int(ph_match.group(1))

    # 提取氯离子含量
    cl_match = re.search(r'氯离子含量(\d+)mg/L', text)
    if cl_match:
        data['氯离子含量'] = int(cl_match.group(1))

    # 提取火焰颜色和焰高
    fire_match = re.search(r'火焰呈([\u4e00-\u9fa5]+)色，焰高(\d+\.\d+)～(\d+\.\d+)m', text)
    if fire_match:
        data['火焰颜色'] = fire_match.group(1)
        data['焰高'] = f"{fire_match.group(2)}～{fire_match.group(3)}m"

    # 提取瞬时气量
    gas_match = re.search(r'估瞬时气量(\d+\.\d+)×104m³/d', text)
    if gas_match:
        data['瞬时气量'] = float(gas_match.group(1)) * 10000  # 转换为标准单位

    # 提取放空气量
    empty_gas_match = re.search(r'放空气量约(\d+\.\d+)×104m³', text)
    if empty_gas_match:
        data['放空气量'] = float(empty_gas_match.group(1)) * 10000  # 转换为标准单位

    # 提取累计放空气量
    total_empty_gas_match = re.search(r'累计放空气量(\d+\.\d+)×104m³', text)
    if total_empty_gas_match:
        data['累计放空气量'] = float(total_empty_gas_match.group(1)) * 10000  # 转换为标准单位

    # 提取B环空压力
    b_press_match = re.search(r'B环空压力(\d+)MPa', text)
    if b_press_match:
        data['B环空压力'] = int(b_press_match.group(1))

    return data




if __name__ == "__main__":
    # 提取原始数据中的信息
    text = """永浅202-1-H3井:(未钻磨桥塞）08:00～10:00开套，经捕屑器、除砂器、分离器放喷排液，套压1.30↑1.35MPa；出口股状液、微量砂，排液量:6.27m³，累计排液量1504.52m³，占应排液19660.75m³的7.65%，余液量18156.23m³，密度1.01g/cm，粘度26s，PH6，氯离子含量2601mg/L；火焰呈橘红色，焰高1.0～2.0m，估瞬时气量0.4245×104m³/d，放空气量约0.0354×104m³，累计放空气量1.6003×104m³；B环空压力0MPa。"""

    # 获取当前日期作为默认日期
    today = datetime.now().strftime('%Y-%m-%d')

    # 提取数据
    extracted_data = extract_data(text)

    # 创建DataFrame
    df = pd.DataFrame([extracted_data])

    # 添加日期列（假设是今天）
    df['日期'] = today

    # 重新排列列顺序，将日期放在前面
    columns = ['日期', '开始时间', '结束时间', '套压', '排液量', '累计排液量', '应排液量', '排液占比', '余液量',
               '密度', '粘度', 'PH值', '氯离子含量', '火焰颜色', '焰高', '瞬时气量', '放空气量', '累计放空气量',
               'B环空压力']
    df = df[columns]
    print(df)
    # 检查是否存在Excel文件，如果存在则读取并追加数据，如果不存在则创建新文件
    try:
        existing_df = pd.read_excel('C:\\Users\\Administrator\\Documents\\test\\永浅202-1-H3井试油汇报致密油汇报.xlsx')
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        combined_df.to_excel('永浅202-1-H3井试油汇报致密油汇报.xlsx', index=False)
        print("数据已追加到现有Excel文件。")
    except FileNotFoundError:
        df.to_excel('永浅202-1-H3井试油汇报致密油汇报.xlsx', index=False)
        print("已创建新的Excel文件并写入数据。")
