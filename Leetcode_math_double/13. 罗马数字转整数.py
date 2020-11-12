class Solution:
    def romanToInt(self, s: str) -> int:
        # ans = 0
        # while s[0] == 'M':
        #     ans += 1000
        #     s = s[1:]
        # while s[:1] == 'CM':
        #     ans += 900
        #     s = s[2:]
        # while s[0] == 'D':
        #     ans += 500
        #     s = s[1:]
        # while s[:1] == 'CD':
        #     ans += 400
        #     s = s[2:]
        # while s[0] == 'C':
        #     ans += 100
        #     s = s[1:]
        # while s[:1] == 'XC':
        #     ans += 90
        #     s = s[2:]
        # while s[0] == 'L':
        #     ans += 50
        #     s = s[1:]
        # while s[:1] == 'XL':
        #     ans += 40
        # while s[0] == 'X':
        #     ans += 10
        # while s[:1] == 'IX':
        #     ans += 9
        # while s[0] == 'V':
        #     ans += 5
        # while s[:1] == 'IV':
        #     ans += 4
        # while s[0] == 'I':
        #     ans += 1
        # return ans

#   不删掉这个看看掌握字典的重要性
        ans = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s) - 1):
            if dic[s[i]] > dic[s[i + 1]]:
                ans += dic[s[i]]
            else:
                ans -= dic[s[i]]
        ans += dic[s[len(s)-1]]

