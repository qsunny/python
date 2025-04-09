import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans


if __name__ == "__main__":

    X = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
    # print(X)
    y = np.array([0, 1, 0])  # 0 类别和 1 类别
    # print(y)

    # test_size = 0.3参数指定了测试集的大小应该是原始数据集的 30%。这意味着70%的数据将被用作训练集，剩下的30% 将被用作测试集。
    # random_state = 42 参数是一个随机数种子，用于确保每次分割数据集时都能得到相同的结果。这在实验和模型验证中非常有用，因为它确保了结果的可重复性。
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 机器学习模型大致分为两大类：监督学习和无监督学习
    # 常见的监督学习任务包括分类和回归
    # 分类（Classification）：将数据点分配到预定的类别中。例如，判断邮件是垃圾邮件还是非垃圾邮件。
    # 回归（Regression）：预测连续值输出。例如，预测房价、气温等。
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # print(y_pred)

    # 无监督学习（Unsupervised Learning）：无监督学习是指没有标签数据，模型仅通过输入数据本身的特征进行学习。
    # 常见的无监督学习任务包括聚类和降维。

    # 聚类（Clustering）：将数据分组，使得同一组中的数据具有相似性。常见的聚类算法包括 K - Means、DBSCAN 等。
    # 降维（Dimensionality Reduction）：减少数据中的特征数量，通常用于数据压缩或可视化。常见的降维方法有 PCA（主成分分析）和 t - SNE（t - 分布随机邻域嵌入）等

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X_train)
    y_pred = kmeans.predict(X_test)
    print(y_pred)