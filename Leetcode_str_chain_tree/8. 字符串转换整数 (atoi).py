class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()   #直接这样去空格不香吗
        if not str or str == '+' or str == '-' or str == ' ':
            return 0
        # return int(str)
        start = 0
        if not str[start].isdigit() and str[start] != '+' and str[start] != '-' :
            return 0
        ans = str[start]
        for i in range(start+1, len(str)):
            if str[i].isdigit():
                ans += str[i]
            else:
                break
        # return int(ans) if -2**31 <= int(ans) < 2**31-1 else 2**31-1
        if  ans == '+' or ans == '-':
            return 0
        num = int(ans)
        if num <= -2147483648:
            num = -2147483648
        if num >= 2147483648:
            num = 2147483647
        return num


str = ' -43'
print(Solution().myAtoi(str))