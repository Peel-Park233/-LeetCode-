def max_length(nums):
    if len(nums) <= 1:
        return len(nums)
    m = len(nums)
    ans = 0
    for i in range(m):
        temp = []
        # print(ans)
        for j in range(i, m):
            if nums[j] not in temp:
                temp.append(nums[j])
            else:
                # ans = max(ans,len(temp))
                break
        ans = max(ans, len(temp))
    return ans
nums = 'dnasdujkdanfluilus'
print(max_length(nums))
#   所以说大问题是没有的
