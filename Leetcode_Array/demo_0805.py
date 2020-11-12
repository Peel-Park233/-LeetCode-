array = [[1, 2, 3], [4, 5, 6]]
print(len(array))
print(len(array[0]))
print((2+3)//2)
print(10%3)
print(10//3)

matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
matrix[0] = matrix[1] +matrix[0]  # 这个语法还挺好用，列表中直接加一个树或者一行数
print(matrix[0])
a = [2, 3]
k = [[2, 3, 4], [2]]
if a in k:
    print('1')
else:
    print(0)

import numpy as np
print(np.random.randint(0, 3, size=14))