# https://ithelp.ithome.com.tw/articles/10197110
# https://zh.wikipedia.org/wiki/%E5%AE%89%E5%BE%B7%E6%A3%AE%E9%B8%A2%E5%B0%BE%E8%8A%B1%E5%8D%89%E6%95%B0%E6%8D%AE%E9%9B%86
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris = datasets.load_iris()
iris_data = iris['data']
iris_label = iris['target']

train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label, test_size=0.2)
knn = KNeighborsClassifier()
knn.fit(train_data, train_label)
test_data_predict = knn.predict(test_data)
print(test_data_predict)
print(test_label)