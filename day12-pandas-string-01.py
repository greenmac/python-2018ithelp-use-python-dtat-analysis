# https://ithelp.ithome.com.tw/articles/10194852

# print("HELLO WORLD".lower()) # lower()讓字串全部變成小寫
# print("hello world".upper()) # upper() 讓字串全部變成大寫
# print("hello world".title()) # title() 讓字串第一個字為大寫
# print(len("hello world")) # len() 得到字串長度

import pandas as pd

bigmac = pd.read_csv('big-mac-raw-index.csv')
bigmac['name'] = bigmac['name'].astype('category')
bigmac['iso_a3'] = bigmac['iso_a3'].str.title()
print(bigmac.head())