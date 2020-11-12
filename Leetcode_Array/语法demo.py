# x,y 分别向上下左右操作
ans = 10
for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    print(ans+x, ans-y)
n = 9
total = ''
for i in range(1, n + 1):
    total += str(i)
print(total)

print(int(3.6))
print(3.6%2)
print(3 // 2)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = a.index(10)
print(p)

#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     :
# @Author   : liyi
# @File     :

# 在快排的同时按同样的排序算法对另一个数组进行操作


# def quick_sort(array, cid_list, left, right):
#
#     if left >= right:
#         return [array,cid_list]
#     low = left
#     high = right
#     key = array[low]
#     cid_key = cid_list[low]
#     while left < right:
#         while left < right and array[right] > key:
#             right -= 1
#         array[left] = array[right]
#         cid_list[left] = cid_list[right]
#         while left < right and array[left] <= key:
#             left += 1
#         array[right] = array[left]
#         cid_list[right] = cid_list[left]
#     array[right] = key
#     cid_list[right] = cid_key
#     quick_sort(array, cid_list, low, left - 1)
#     quick_sort(array, cid_list, left + 1, high)
#     return [array, cid_list]
#
#
# if __name__ == '__main__':
#     test = [1, 5, 6, 2]
#     cid_list = [6, 5, 3, 8]
#     print(quick_sort(test, cid_list, 0, 3))
#     print(test)
#     print(cid_list)
test = [1, 5, 6, 2]
cid_list = [6, 5, 3, 8]
# total = [test, cid_list]
total = []
for i in range(len(test)):
    total.append([test[i], cid_list[i]])
print(total)
total.sort()
print(total)