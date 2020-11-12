class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ['' for _ in range(numRows)]
        flag = 1    # 这个flag立的好,Z字形转来转去
        j = 0
        for i in range(len(s)):
            res[j] += s[i]
            j += flag
            #   确定什么时候要转向
            if j == numRows - 1 or j == 0:
                flag = - flag
        ans = ''
        for k in range(numRows):
            ans += res[k]
        return ans

s = "LEETCODEISHIRING"
numRows = 3
print(Solution().convert(s, numRows))