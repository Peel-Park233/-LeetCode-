class Solution(object):
    def fourSum(self, nums, target):
        #   双指针,应该是for在外面，while在里面，刚开始写错了
        ans = []
        nums.sort()
        m = len(nums)
        for i in range(m-3):
            for j in range(i+1, m-2):
                low = j + 1
                high = m - 1
                while high > low:
                    s = nums[i] + nums[j] + nums[low] + nums[high]
                    if s > target:
                        high -= 1
                    elif s < target:
                        low += 1
                    else:
                        if [nums[i], nums[j], nums[low], nums[high]] not in ans:
                            ans.append([nums[i], nums[j], nums[low], nums[high]])
                        #   若后面的数和这个数相同，指针往后移动一位
                        while low < high and nums[low] == nums[low + 1]: low += 1
                        while low < high and nums[high] == nums[high - 1]: high -= 1
                        #   直到数不相同了，都移动到那个不相同的数
                        low += 1
                        high -= 1


        return ans


nums = [1, 0, -1, 0, -2, 2]
target = 0

print(Solution().fourSum(nums, target))

#   这题会做了，那么三数之和也会做了
