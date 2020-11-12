import numpy as np
print(np.random.randn(2, 2))

path = ['aabb', 'dsada']
print(path)
path.pop()
print(path)
number_str = {'2': "abc", '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

print(number_str['3'])
digits = '23'
for k in digits:
    print(number_str[k])
print(5//2)
temp = [0, 1, 2, 3]
i = 0
print(temp[:1])  # 左闭右开

formal = [2, 3, 4, 5]
k = [6]
print(formal + k)

A = []
for i in A:
    print(i)

# B = '1'
# print(type(B))
# print(type(B) == 'int')
B = '101101101'
m = 5
n = 3
for i in B:
    if i == '1':
        m -= 1
    if i == '0':
        n -= 1
print(m, n)
print([2*[0] for i in range(8)])
m = 5
n = 3
dp = [[0 for i in range(n)] for i in range(m)]
print(dp)

data = [1, 2, 3, 4, 5, 6, 7]
print(data.pop(1))
print(data)

data = [1, 2, 3]
print(data[0+1:])

data = []
data += [1]
data += [2]
print(data)


def plus(i, j):
    return i + j


def add(a, b):
    return a + b
print(plus(1, add(1, 2)))
#    函数里面也可以调用函数，这样不用回溯也可以了
