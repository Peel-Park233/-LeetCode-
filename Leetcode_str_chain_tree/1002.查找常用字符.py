# str=input()
# resoult={}
# for i in str:
#     resoult[i]=str.count(i)
# print(resoult)
# a = 'dasdasd'
# a = list(a)
# a.sort()
# print(a)
# A = 'dasdasd'
# A = list(A)
# A.pop(1)
# print(A)
# import numpy as np
# A = np.random.randn(5,5)
# for i in range(len(A)):
#     A[i].append(0)
# print(A)
def commonChars(A):
    ans = []
    for k in range(A[0]):

        for i in range(1, len(A)):
            if A[0][k] not in A[i]:
                break
            if i == len(A)-1:
                A[i] = A[i].replace(A[0][k], '', 1) # 通过用空格替换的方式来删除
    return ans

