from typing import List # 这个要记住
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(temp, number):
            if not number:
                if temp not in ans:
                    ans.append(temp)
                return
            for i in range(len(number)):
                dfs(temp + [number[i]], number[:i] + number[i+1:])
        dfs([], nums)
        return ans

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))


#   这题最重要是想到单步循环是怎么样的