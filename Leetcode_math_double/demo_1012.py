class Solution:
    def max_length(self, nums):
        if len(nums) <= 1:
           return len(nums)
        m = len(nums)
        ans = 0
        for i in range(m):
            temp = []
            print(ans)
            for j in range(i,m):
                if nums[j] not in temp:
                    temp.append(nums[j])
                else:
                    # ans = max(ans,len(temp))
                    break
            ans = max(ans, len(temp))

        return ans
nums = 'dasdbuqw'
print(Solution().max_length(nums))
#   叫test_1012所以就运行测试框架了。。。。，改成demo_1012就好了