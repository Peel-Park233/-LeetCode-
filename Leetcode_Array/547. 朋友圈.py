class Solution:
    def findCircleNum(self, M):
        n = len(M)
        self.ans = 0
        def find_friend(i):
            # print(M)
            if M[i][i] == 1:
                self.ans += 1
                M[i][i] = 0
            for k in range(n):
                if M[i][k] == 1:
                    M[i][k] = 0
                    M[k][k] = 0
                    find_friend(k)
        for i in range(n):
            find_friend(i)
        return self.ans


M =[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 1]]
print(Solution().findCircleNum(M))


#   太对了哥，传递后设置为0嘛