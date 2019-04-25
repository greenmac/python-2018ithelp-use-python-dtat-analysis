# https://ithelp.ithome.com.tw/articles/10197461
"""
為什麼需要交叉驗證
為了避免依賴某一特定的訓練和測試資料產生偏差。
"""
from sklearn.model_selection import cross_val_score
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris['data']
y = iris['target']

"""
只測試一種n_neighbors
"""
# knn = KNeighborsClassifier(n_neighbors=10)
# # 而這裡的cv=5是分成5組的意思。'accuracy'則是一種方法，是顯示準確度高不高的方法（越高越好）
# scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
# # print(scores)
# # print(scores.mean())

"""
測試多種n_neighbors
"""
# 改變n_neighbors
k_range = range(1, 31)
k_scores = []
for k_number in k_range:
    knn = KNeighborsClassifier(n_neighbors=k_number)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())

plt.plot(k_range,k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()