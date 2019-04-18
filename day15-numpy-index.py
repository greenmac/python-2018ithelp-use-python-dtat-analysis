# https://ithelp.ithome.com.tw/articles/10195645
import numpy as np

arr = np.arange(10)
# print(arr[5:8])

arr[5:8] = 7
# print(arr)

myarr = np.arange(10)
myarry_slice = myarr[5:8]
myarr[5:8] = 7
myarry_slice[1] = 87
print(myarr)