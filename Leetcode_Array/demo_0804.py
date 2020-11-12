n = 2
m = 3
# matrix = [0]*n
# for i in range(len(matrix)):
#   matrix[i] = [0]*m
# print(matrix)

# mat = m * [0]
# for i in range(len(mat)):
#     mat[i] = n * [0]  # 每一行有这么多个
#
# 创建一个m*n的哈希表，可以简化为
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
print(dp)

#   创建一个不同长度的初始哈希表
n = 4
mat = [i*[0] for i in range(1, n+1)]
print(mat)
print(5//4)

