from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = []
        for i in nums1:
            total.append(i)
        for j in nums2:
            total.append(j)
        total.sort()
        # print(total)
        if len(total) % 2 == 0:
            index_1 = len(total) // 2
            index_2 = len(total) // 2 - 1
            ans = (int(total[index_1]) + int(total[index_2]))/2
            return ans
        else:
            return total[len(total) // 2]

nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))

#   真就菜鸡方法
