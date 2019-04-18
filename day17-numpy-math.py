# https://ithelp.ithome.com.tw/articles/10195984
import numpy as np

x1 = np.random.randn(2, 4)+1.920929
# print(x)

x2 = np.random.randint(4, size=10) # 產生<4的整數，大小為10
# print(x2)
x3 = np.random.randint(low=4, high=10, size=10) # 這樣就會產生大小為10，從4到小於10（9）的整數
# print(x3)

x = np.random.randn(5, 4)
# print(x.mean())

x = np.random.randn(5, 4)
# print(x.sum())

x_min = np.random.randn(5, 4)
# print(x_min)
# print(x_min.min())

x_max = np.random.randn(5, 4)
# print(x_max)
# print(x_max.max())

"""
第一個index為2 = 2
第二個index為2+3 = 5
第三個index為2+3+4 = 9
第四個index為2+3+4+5 = 14
"""
x = np.array([[2,3,4], [5,6,7]])
# print(np.cumsum(x)) # [ 2  5  9 14 20 27]

x = np.array([[1, 2], [3, 4]])
print(np.std(x)) # 標準差