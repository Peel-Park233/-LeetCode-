# 题目描述: 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1）
# 每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？


class Solution:
    def cuttingRope(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        times = n // 3
        other = n % 3
        if other == 2:
            ans = (3 ** times) * other
        elif other == 1:
            ans = (3 ** (times-1)) * 4
        else:
            ans = (3 ** times)

        return ans


if __name__ =='__main__':
    n = 10
    print(Solution().cuttingRope(n))

#   思路：发现了4以及以上都是切分更大，那切成3不就是最大的，然后加一些特判就ok了
