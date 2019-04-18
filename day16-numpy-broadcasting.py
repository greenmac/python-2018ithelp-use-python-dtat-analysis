# https://ithelp.ithome.com.tw/articles/10195830
import numpy as np

a = np.array([1,2,3])
b = np.array([2,2,2])
# print(a * b)

c = np.array([1.0, 2.0, 3.0])
d = 2
# print(c * d)

x = np.arange(4)
xx = x.reshape(4, 1)
y = np.ones(5)
# print(xx + y)

s = np.arange(6)
s = s.reshape((3, 2))
# print(s)

x = np.zeros((10, 2))
# print(x)
y = x.T
# print(y)

x = np.array([[3, 4], [5, 6]])
x = x.T
# print(x)

y = np.array([1,2,3,4])
# print(y.base is None) # True

x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
(xx + y)
# print(xx.base is x) # True

x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
(xx + y)
print(xx.base is y) # False