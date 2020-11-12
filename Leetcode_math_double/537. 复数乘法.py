# 题目描述:
# 给定两个表示复数的字符串。 返回表示它们乘积的字符串。注意，根据定义 i**2 = -1 。


class Solution:
    def complexNumberMultiply(self, a, b):
        a, b = a.split('+'), b.split('+')     # 最关键的一步，要把字符串分割成能用的列表
        print(a)
        print(type(a))
        ans_real = int(a[0])*int(b[0])-int(a[1][:-1])*int(b[1][:-1])
        ans_imag = int(a[0])*int(b[1][:-1])+int(b[0])*int(a[1][:-1])
        ans = str(ans_real) + '+' + str(ans_imag) + 'i'

        return ans   # 直接返回能省那么多内存空间吗，学到了


a = "1 + 1i"
b = "1 + 1i"
print(Solution().complexNumberMultiply(a, b))

#   思路：把字符串分割成能用的列表，以及字符串连接的方法
