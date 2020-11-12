# 题目描述: 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。


class Solution:
    def isSubsequence(self, s, t):
        m = len(s)
        n = len(t)
        #   就是这两个双指针，一个指向长数组的位置,一个指向分数。不过不是这么做的
        ip = -1
        score = 0
        for i in range(m):
            for j in range(ip + 1, n):
                if s[i] == t[j]:
                    score += 1
                    ip = j
                    break    #
                # if s[i] != t[-1]:
                #     return False
            # else:         # 这样简化后就不需要记录score了，节省了空间
            #     return False
            print(score)
        if score == len(s):
            return True
        else:
            return False


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))


