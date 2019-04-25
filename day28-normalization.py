# https://ithelp.ithome.com.tw/articles/10197357
from sklearn import preprocessing
import numpy as np

# 用train_test_split來把資料做切分（一邊為訓練一邊為測試資料）
# 用make_classification用來產生隨機的訓練資料
# 用SVC這個分類法當作例子

from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt

X,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,
                          random_state=3,scale=100,n_clusters_per_class=1)
# 會看到下圖，有兩部分的資料，因為我們設定了n_features=2
# plt.scatter(X[:,0],X[:,1],c=y)
# plt.show()
"""
未標準化
"""
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# clf = SVC()
# clf.fit(X_train, y_train)

# clf_score = clf.score(X_test, y_test)
# # print(clf_score)

"""
標準化
"""
# 證明標準化能夠讓幫助資料訓練，我們使用preprocessing.scale()標準化X
X = preprocessing.scale(X)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
clf = SVC()
clf.fit(X_train,y_train)

clf_score = clf.score(X_test, y_test)
print(clf_score)