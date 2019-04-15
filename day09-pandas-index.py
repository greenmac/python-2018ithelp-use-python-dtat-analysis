# https://ithelp.ithome.com.tw/articles/10194006
import pandas as pd
import numpy as np

# bond = pd.read_csv('./James Bond 007 Movie Data.csv')
# bond = pd.read_csv('./James Bond 007 Movie Data.csv',index_col='Film')


# bond = pd.read_csv('./James Bond 007 Movie Data.csv',index_col='Film').head()
# print(bond.index)

# bond = pd.read_csv('./James Bond 007 Movie Data.csv')
# bond.set_index('Film', inplace=True)
# # bond.reset_index(inplace=True) # reset_index()可以讓index重置成原本的樣子
# print(bond.head())

# bond = pd.read_csv('./James Bond 007 Movie Data.csv',index_col='Film')
# print(bond.loc[['Goldfinger', 'From Russia With Love']])

# bond = pd.read_csv('./James Bond 007 Movie Data.csv')
# # print(bond.iloc[15])
# print(bond.iloc[[0, 4]])
# print('==========')
# print(bond[0:4])

# bond = pd.read_csv('./James Bond 007 Movie Data.csv',index_col='Film')
# bond.rename(columns={'Year':'Release Date', "Box Office":"Revenue"}, inplace=True) # 從新命名欄
# bond.rename(index={
#     "Dr. No":"Doctor No",
#     "GoldenEye":"Golden Eye",
#     "The World Is Not Enough":"Best bond Movie Ever"
# }, inplace=True) # 從新命名列
# print(bond)

## axis=1跟axis="columns"是一樣的！axis=0則是和asxis = "row"一樣。
bond = pd.read_csv('./James Bond 007 Movie Data.csv')
bond.drop(labels=["Actual box office","Bond actor"], axis="columns")
print(bond)
