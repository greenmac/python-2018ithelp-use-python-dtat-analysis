# https://ithelp.ithome.com.tw/articles/10193421
import pandas as pd

# df = pd.read_csv('./train.csv')
# # print(df.head())
# # print(df.tail())
# # print(df.shape)
# # print(df.Name[0:4])
# # print(df[['Name', 'Sex']])
# df.insert(3, column='sport', value='Basketball')
# # print(df.head())


titanic = pd.read_csv('./train.csv')
# titanic = titanic.dropna()
# print(titanic.head())
# titanic = titanic.fillna(0)
# print(titanic.head())
titanic = titanic.sort_values('Name', ascending= False) # ascending= False 反序
print(titanic.head())