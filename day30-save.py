# https://ithelp.ithome.com.tw/articles/10197575
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib


clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris['data'], iris['target']
clf.fit(X, y)
"""
save
"""
# joblib.dump(clf, './data/clf.pkl')

"""
load
"""
clf2 = joblib.load('./data/clf.pkl')
clf2_predict = clf2.predict(X[0:100])

# print(X[0:10])
print(clf2_predict)