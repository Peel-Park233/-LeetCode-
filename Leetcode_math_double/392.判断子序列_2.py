# 题目描述: 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。


class Solution:
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
    #   这一段可以简化为：return i==len(s)
    #     if i == len(s):
    #         return True
    #     else:
    #         return False
        return i == len(s)


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))

# 要点：双指针这个代码就很清晰，漂亮
