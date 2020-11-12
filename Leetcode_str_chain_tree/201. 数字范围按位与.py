class Solution:
    def rangeBitwiseAnd(self, m: int, n: int):
        s = bin(m)
        l = len(s)
        firstindex = -1
        if n >= int('0b1' + (l-2)*'0', 2):  # 若比它多一位，那么每一位必定是0
            return 0
        for i in range(3, l):
            if s[i] == '1':
                if s[i - 1] == '0':
                    checks = s[:i-1] + '10' + '0'*(l - i - 1)
                    if int(checks, 2) <= n:
                        firstindex = i
                        break
        if firstindex == -1:
            return m
        return int(s[:firstindex-1] + '0'*(l-firstindex+1), 2)


if __name__ == '__main__':
    m = 5
    n = 7
    print(Solution().rangeBitwiseAnd(m, n))