class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [1 for i in range(n)]   #   用来记录n-1！阶乘
        for i in range(1, n):
             nums[i] = nums[i-1]*i
        # print(nums)
        ans = ''
        k = k - 1   #
        s = [i for i in range(1, n+1)]
        for i in range(n - 1, -1, -1):
            number = s[k//nums[i]]
            del s[k // nums[i]]  # 删除这个元素
            # print(number)
            k = k % nums[i]
            ans += str(number)
            # print(s)

        return ans

print(Solution().getPermutation(7, 2020))