from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
https://www.runoob.com/sklearn/sklearn-iris-dataset.html
"""

if __name__ == "__main__":
    # 加载鸢尾花数据集
    data = load_iris()

    # 转换为 DataFrame 方便查看
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    df['species'] = df['target'].apply(lambda x: data.target_names[x])

    # 查看前几行数据
    #print(df.head())
    # 绘制特征之间的关系
    # sns.pairplot(df, hue="species")
    # plt.show()

    # 绘制特征之间的关系
    correlation_matrix = df.drop(columns=['target', 'species']).corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()