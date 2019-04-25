# https://ithelp.ithome.com.tw/articles/10197248
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets

# 使用make_regression()方法，建立200個樣本(samples)，
# 只有一種特徵(features)和一種標籤類別（label），我們將noise設為10，這樣資料會比較分散一點
X, y = datasets.make_regression(n_samples=200, n_features=1, n_targets=1, noise=10)

# plt.scatter(X, y, linewidths=0.1)
# plt.show()

model = LinearRegression()
model.fit(X, y)

predict = model.predict(X[:200, :])

plt.plot(X, predict, c='red')
plt.scatter(X, y)
plt.show()