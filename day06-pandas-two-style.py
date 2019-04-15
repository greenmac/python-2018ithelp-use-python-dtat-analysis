# https://ithelp.ithome.com.tw/articles/10193394
import pandas as pd

# my_obj = pd.Series([4, 7, -5, 3])
# print(my_obj.values)
# print(my_obj.index)

# my_obj2 = pd.Series([8, 9 , 10, 11], index=['a', 'b', 'c', 'd'])
# print(my_obj2.a)
# print('a' in  my_obj2)

# dic_data = {'name':'apple','birthday':'1996-1-1','luckynumber':7 }
# my_obj3 = pd.Series(dic_data)
# print(my_obj3)

# registration = [True,False,True,True]
# registration = pd.Series(registration)
# print(registration)

data = {'name':['Bob', 'Nancy','Amy','Elsa','Jack'],
        'year':[1996, 1997, 1997, 1996, 1997],
        'day':[11,23,8,3,11],
        'month': [8, 8, 7, 1, 12],
}
myframe = pd.DataFrame(data)
# print(myframe)
myframe2 = pd.DataFrame(data, columns=['name','year', 'month', 'day'])
# print(myframe2)
myframe3 = pd.DataFrame(data, columns=['name','year', 'month', 'day', 'luckynumber'])
luckynumber = ['3','2','1','7']
luckynumber = pd.Series(luckynumber)
myframe3['luckynumber'] = luckynumber
print(myframe3)