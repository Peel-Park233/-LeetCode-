class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_1 = s[::-1]
        m = len(s)
        dp = [0 for _ in range(m+1)]    # 多一格
        ans = 0
        for i in range(m):
            if s[i] == s_1[i]:
                if dp[i] == 0:
                    dp[i+1] = 1
                else:
                    dp[i+1] = dp[i] + 1
        #   dp里面最大值的位置减去他的数值就是这段回文串
        print(dp)
        a = max(dp)
        b = dp.index(a)     # 就是得到第一个和这个数相同的位置
        return s[b-a:b]


s = "babad"
print(Solution().longestPalindrome(s))