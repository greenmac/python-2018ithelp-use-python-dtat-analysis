# https://ithelp.ithome.com.tw/articles/10197029
from sklearn import tree

# 將皺用1表示、平滑用0表示。橘子用0、蘋果用1，用這種資料格式餵給電腦可以讓電腦容易理解。
features = [[150, 1], [170, 1], [130, 0], [140, 0]]
labels = [0, 0, 1, 1]

## DecisionTreeClassifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

wantPredict = clf.predict([[120, 0]])
if wantPredict == [1]:
    print('This is an apple')
elif wantPredict == [0]:
    print('This is an orange')