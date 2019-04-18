# https://ithelp.ithome.com.tw/articles/10195434
import numpy as np

# data = np.array(
#     [[ 0.226, -0.23 , -0.86],
#     [ 0.5639, 0.2379, 0.904]]
# )

# data = np.array([1, 2, 3], dtype=complex)

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2_ndim = arr2.ndim
arr2_shape = arr2.shape
arr2_atype = arr2.dtype
print(arr2_atype)