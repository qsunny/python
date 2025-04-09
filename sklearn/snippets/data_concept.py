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

if __name__ == "__main__":

    X = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [2.0, 4.0], [2.0, 3.0]])
    print(X)
    y = np.array([0, 1, 0, 1, 0])  # 0 类别和 1 类别
    print(y)
    # 预处理与特征工程
    # 标准化（Standardization）：特征的尺度统一，使得每个特征都具有零均值和单位方差。
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print(X_scaled)

    # 归一化（Normalization）：将特征的值缩放到一个固定范围（通常是0到1）。
    scaler = MinMaxScaler()
    X_normalized = scaler.fit_transform(X)
    print(X_normalized)

    # 类别变量编码：将类别型数据转换为数值型数据（如one-hot编码）

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # 模型评估与验证
    scores = cross_val_score(clf, X, y, cv=2)  # 5-fold cross-validation
    print("Cross-validation scores:", scores)

    '''
    分类任务的评估指标：
    准确率（Accuracy）：预测正确的样本占所有样本的比例。
    精确率（Precision）：正类预测中，实际正类的比例。
    召回率（Recall）：实际正类中，正确预测的比例。
    F1分数：精确率和召回率的调和平均数。
    '''

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("precision_score :", precision_score(y_test, y_pred, zero_division=1))
    print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))

    '''
    回归任务的评估指标：    
        均方误差（MSE）：预测值与真实值的平方差的平均值。
        决定系数（R²）：衡量模型对数据变异的解释能力。
    '''
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R²:", r2_score(y_test, y_pred))

    # 模型选择与调优
    # 网格搜索是一种常用的超参数调优方法，它通过遍历所有可能的参数组合来寻找最佳的超参数组合
    param_grid = {'max_depth': [3, 5, 7], 'min_samples_split': [2, 5, 10]}
    grid_search = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=2)
    grid_search.fit(X_train, y_train)
    print("Best parameters:", grid_search.best_params_)

    # 随机搜索是一种通过随机选择超参数的组合来搜索最优超参数的方法，它比网格搜索效率高。
    param_dist = {'max_depth': [3, 5, 7], 'min_samples_split': randint(2, 10)}
    random_search = RandomizedSearchCV(DecisionTreeClassifier(), param_dist, n_iter=10, cv=2)
    random_search.fit(X_train, y_train)
    print("Best parameters:", random_search.best_params_)