class Solution:
    def reverseWords(self, s: str):
        s = [i for i in s.split()]
        # return s
        m = len(s)
        print(s[0])
        ans = []
        for i in range(m):
            # print(i)
            L = s[i]
            L = L[::-1]
            ans.append(L)
        ans = ' '.join(ans)
        return ans


s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))