class Solution:
    def findSubsequences(self, nums):
        if len(nums) < 2:
            return []
        # 递归怎么说
        ans = set()     # 哈希表
        #  主要思想，分成两部分，第一部分是已有的，第二部分是可以添加的
        def increase(formal, last):
            #  退出循环的条件
            if len(formal) >= 2:
                # print(formal)
                ans.add(tuple(formal))
            for i in range(len(last)):
                if last[i] >= formal[-1]:
                    increase(formal + [last[i]], last[i+1:])
        #   从哪个起点开始遍历
        for i in range(len(nums) - 1):
            # print(type(nums))
            increase([nums[i]], nums[i+1:])
        return list(ans)


nums = [4, 6, 7, 7]
print(Solution().findSubsequences(nums))

# 仔细想一想确实暴力法不行，第一个指针指向第一个点，第二个指向第二个点（若第二个大于第一个点）...这样就会有很多。
