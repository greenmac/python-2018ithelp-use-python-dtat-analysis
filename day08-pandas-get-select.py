# https://ithelp.ithome.com.tw/articles/10194003
import pandas as pd
import numpy as np

seriesObj = pd.Series(range(10), index=['a', 'a', 'b', 'b', 'b','c','c','c','c','c'])
# print(seriesObj['c'])

df = pd.DataFrame(np.random.randn(4, 2), index=['a', 'a', 'b', 'b'])
# print(df.ix['b'])

titanic = pd.read_csv('./train.csv')
# print(titanic)
fliter = (titanic['Sex'] == 'male')
# titanic[fliter]
print(titanic[fliter])