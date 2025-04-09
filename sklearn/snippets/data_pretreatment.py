import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, classification_report, precision_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler


"""
https://www.runoob.com/sklearn/sklearn-data-preprocessing.html
pip install imblearn
"""
if __name__ == "__main__":

    X = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]])
    # print(X)
    y = np.array([0, 1, 0, 1, 0])  # 0 类别和 1 类别
    # print(y)
    # 检查缺失值

    df = pd.DataFrame(X, columns=['Name', 'Age'])
    # 假设我们有一个 DataFrame df
    print(df.isnull().sum())  # 查看每一列缺失值的数量

    '''
    填充缺失值
    对于缺失值的处理，最常用的方法是填充。
    常见的填充策略包括：
    填充均值（Mean）：适用于数值型数据。
    填充中位数（Median）：对于含有离群值的数据集，使用中位数可能更有效。
    填充最频繁值（Mode）：适用于类别型数据。
    '''
    # 对于数值型数据，使用均值填充
    imputer = SimpleImputer(strategy='mean')  # 可选：'mean', 'median', 'most_frequent'
    df_imputed = imputer.fit_transform(df)  # 填充缺失值
    # 如果缺失值的数量较少，并且删除这些数据不会显著影响分析结果，另一种选择是直接删除缺失值。
    df_cleaned = df.dropna()  # 删除包含缺失值的行

    # 机器学习算法对数据的尺度敏感，因此需要对数据进行缩放，使得特征具有相同的尺度。
    # 常见的缩放方法有：
    # 标准化（Standardization）：将数据转换为均值为 0、标准差为1的分布。适用于大多数机器学习算法。
    # 归一化（Normalization）：将数据缩放到指定范围（通常是[0, 1]）
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)  # 标准化 X

    scaler = MinMaxScaler()
    X_normalized = scaler.fit_transform(X)  # 归一化 X

    '''
    为什么需要标准化和归一化？
    标准化：对于距离度量（如 K 最近邻、支持向量机等）非常重要，因为特征的尺度不一致可能导致某些特征对模型的影响过大。标准化能确保每个特征对模型有相同的贡献。
    归一化：有些算法（如神经网络、梯度下降优化算法等）对输入数据的范围非常敏感，归一化有助于加速收敛。

    类别变量编码
    机器学习模型通常无法直接处理字符串类型的类别变量，因此需要将类别变量转化为数值型数据。
    常见的编码方法有：
    标签编码
    标签编码将每个类别映射到一个唯一的整数。
    适用于类别之间有顺序关系的情况（例如，低、中、高）。
    '''
    # 假设我们有一个类别变量 y
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)  # 将类别变量转换为整数
    # print(y_encoded)

    '''
    独热编码
    独热编码将每个类别转换为一个二进制的向量，适用于类别之间没有顺序关系的情况（例如，颜色、国家等）。
    OneHotEncoder可以将类别变量转化为独热编码。
    '''


    # 假设我们有一个类别变量 X
    encoder = OneHotEncoder(sparse_output=False)  # sparse_output=False 返回一个密集矩阵
    X_encoded = encoder.fit_transform(X)  # 将类别变量转换为独热编码
    # print(X_encoded)
    # 在pandas中，也可以使用get_dummies()函数进行独热编码：
    # X_encoded = pd.get_dummies(X)
    # print(X_encoded)

    # 特征选择
    # 基于模型的特征选择

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    # 训练一个随机森林模型
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # 获取特征重要性
    importances = clf.feature_importances_
    print(importances)

    '''
    递归特征消除（Recursive Feature Elimination，RFE）
    RFE是一种通过递归的方式，逐步删除最不重要的特征，从而选择最优特征的方法。
    RFE可以帮助我们自动选择重要特征。
    '''
    # 使用线性模型进行递归特征消除
    rfe = RFE(clf, n_features_to_select=3)  # 保留 3 个最重要的特征
    X_rfe = rfe.fit_transform(X_train, y_train)
    print(X_rfe)

    '''
    特征工程
    特征工程是通过对现有特征进行处理、组合或构造新的特征，以提高模型的表现。

    特征工程的常见方式包括：
    特征组合：将两个或更多的特征组合成一个新特征。
    特征转换：对特征进行对数变换、平方根变换等，以解决数据的非线性问题。
    特征创建：根据现有数据创建新的特征，例如从时间戳中提取出日期、月份、星期等。
    '''
    # 例如，将两个数值型特征组合成一个新特征
    # df['new_feature'] = df['feature1'] * df['feature2']

    # 特征提取
    # 常见的特征提取方法包括: 主成分分析（PCA） 和 线性判别分析（LDA）。
    # PCA 是一种常用的降维技术，它通过线性变换将数据从高维空间映射到低维空间，使得新特征（主成分）尽可能保留数据的方差。
    # PCA 特别适用于特征数量过多的情况，可以有效降低计算复杂度。

    # 假设 X 是特征矩阵
    pca = PCA(n_components=2)  # 降维到 2 个主成分
    X_pca = pca.fit_transform(X)
    print(X_pca)
    '''
    PCA主要用于两种场景：
        降维：当特征过多时，使用PCA降维可以减少计算成本，同时保留数据的主要信息。
        可视化：将高维数据映射到2D或3D空间，帮助我们可视化数据结构。
    '''

    '''
    线性判别分析（LDA）
    LDA是一种监督学习的降维方法，它旨在找到一个线性组合，使得不同类别之间的距离最大化，类别内的距离最小化。
    LDA通常用于分类任务中。
    '''
    # 假设 X 是特征矩阵，y 是目标变量
    # lda = LinearDiscriminantAnalysis(n_components=2)  # 降维到 2 个线性判别组件
    # X_lda = lda.fit_transform(X, y)
    # print(X_lda)

    '''
    处理不平衡数据在分类问题中，如果数据集的各类别样本数量差异较大，可能会导致模型偏向预测多数类，从而影响模型的性能。
    常见的处理方法包括：
        上采样（Over-sampling）
    通过增加少数类样本的数量，使得数据集更加平衡。
    常见的方法是使用 SMOTE（Synthetic Minority Over-sampling Technique） 算法。
    '''
    # smote = SMOTE()
    # X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    # 下采样（Under - sampling）
    # 通过减少多数类样本的数量，使得数据集更加平衡。
    undersampler = RandomUnderSampler()
    X_resampled, y_resampled = undersampler.fit_resample(X_train, y_train)