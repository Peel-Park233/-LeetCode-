# 题目描述:
# 两个二进制字符输入，输入这两个二进制字符相加的结果

class Solution:
    def addBinary(self, a, b):
        a, b = list(a), list(b)
        a = a[::-1]
        b = b[::-1]
        if len(a) > len(b):
            for _ in range(len(a) - len(b)):
                b.append(0)
        elif len(b) > len(a):
            for _ in range(len(b) - len(a)):
                a.append(0)
        else:
            print('长度相同')
        sum = [0 for _ in range(max(len(a), len(b)) + 1)]
        for i in range(len(b)):
            sum[i] = int(a[i]) + int(b[i])

        for i in range(len(sum) - 1):
            if sum[i] == 0:
                sum[i] = 0
            elif sum[i] == 1:
                sum[i] = 1
            elif sum[i] == 2:
                sum[i+1] += 1
                sum[i] = 0
            else:
                sum[i] = 1
                sum[i+1] += 1
        if sum[-1] == 0:
            sum.pop(-1)
        for i in range(len(sum)):
            sum[i] = str(sum[i])
        sum = sum[::-1]
        return ''.join(sum)

        # return sum


if __name__ == '__main__':
    a = "11001"
    b = "11010"
    print(Solution().addBinary(a, b))


#   思路：把两个列表反转然后设置成长度相同的相加，
#   加完得到的列表再进行判定（0， 1， 2， 3），最后反转转化为字符串输出


