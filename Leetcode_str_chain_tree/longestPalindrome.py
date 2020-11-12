#   题目描述：
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000


class Solution:
    def longestPalindrome(self, s):
        #   没想到还是要用dp来做，就是如果在暴力操作的时候经常涉及到重复的就可以dp
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        maxlength = 0
        start_index = 0
        #   设i是起点， j是终点
        for i in range(length):
            dp[i][i] = True
        for j in range(1, length):
            for i in range(0, j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = dp[i+1][j-1]  # 本来就是在他们里面的一段数，怎么会取不到
                if dp[i][j]:
                    if j - i + 1 > maxlength:
                        maxlength = j - i + 1   # 确实应该加1
                        start_index = i
        print(dp)
        return s[start_index: start_index + maxlength]


if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))

#   要点：最最最关键的就是能想到dp[i][j] 来代表i到j是不是回文，而且dp[i + 1][j - 1]
