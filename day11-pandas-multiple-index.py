# https://ithelp.ithome.com.tw/articles/10194235
import pandas as pd

# bigmac = pd.read_csv('./big-mac-raw-index.csv')
# bigmac.set_index(keys=['date', 'name'], inplace=True)
# # print(bigmac)
# # print(bigmac.index.names)
# print(type(bigmac.index))

# bigmac = pd.read_csv('./big-mac-raw-index.csv', parse_dates=['date'], index_col=['date', 'name'])
# bigmac.sort_index(inplace=True)
# print(bigmac.head(10))
# print(bigmac.index.get_level_values(0)) # [0] = ['date']
# print(bigmac.index.get_level_values('date')) # [0] = ['date']
# print(bigmac.index.get_level_values(1)) # [1] = ['name']
# print(bigmac.index.get_level_values('name')) # [1] = ['name']

bigmac = pd.read_csv('./big-mac-raw-index.csv', parse_dates=['date'], index_col=['date', 'name'])
bigmac.sort_index(inplace=True)
bigmac.index.set_names(['day', 'location'], inplace=True)
print(bigmac.head())