# https://ithelp.ithome.com.tw/articles/10196167
import numpy as np

# x = np.arange(10)
# np.save('./data/my_array', x)
# data = np.load('./data/my_array.npy')
# print(data)

# aData = [1,2,3,4,5,6]
# bData = [7,8,9,10,11,12]
# np.savez('./data/my_archive.npz', a=aData, b=bData)
# myArch = np.load('./data/my_archive.npz')
# print(myArch['b'])
# print(myArch['a'])

myArr = np.loadtxt('./data/my_txt.txt', delimiter=',')
# print(myArr)
np.savetxt('./data/txtfile.txt', myArr)