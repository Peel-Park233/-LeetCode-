class Solution:
    def threeSum(self, nums):

        nums.sort()# 先排序
        print(nums)
        ans = []
        for i in range(1, len(nums) - 1):
            # 双指针法
            low = 0
            high = len(nums) - 1
            while low < i and high > i:
                if nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                elif nums[i] + nums[low] + nums[high] < 0:
                    low += 1
                else:
                    if [nums[low], nums[i], nums[high]] not in ans:
                        ans.append([nums[low], nums[i], nums[high]])
                    low += 1

        return ans


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 1, 1, 2]
    print(Solution().threeSum(nums))
