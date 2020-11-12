from typing import List
class Solution:
    def maxArea(self, height) -> int:
        #   暴力法,盲猜超时
        # m = len(height)
        # ans = 0
        # for i in range(m):
        #     for j in range(i+1, m):
        #         ans = max(ans, (j-i) * min(height[i], height[j]))

        # return ans
        m = len(height)
        low = 0
        high = m -1
        ans = 0
        while(high > low):
            ans = max(ans, (high - low) * min(height[low], height[high]))
            if height[low] > height[high]:
                high -= 1
            else:
                low += 1
        return ans

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))

