class Solution:
    def findLength(self, A, B):
        n = len(A)
        m = len(B)
        score = 0
        for i in range(n):# A从这个点开始的最长子串
            for j in range(m):  # B从这个点开始的最长子串
                k = i
                p = j
                temp = 0
                while p < m and k < n:   # 计算这两个起点开始的最长相同串
                    # print(p)
                    # print(B[p], A[k])
                    if A[k] == B[p]:
                        temp += 1
                        k += 1
                        p += 1
                    else:
                        # score = max(temp, score)
                        # print(score)
                        break
                    score = max(temp, score)
        return score


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    print(Solution().findLength(A, B))

#  暴力法就会超时！！
#  其实确定两个起点之后比较两者的长度可以另外定义个小函数
