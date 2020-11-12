#   重点就是维护一个不重复的最长连续子序列,滑动窗口

s = 'abcabcbb'
ans = 0
nums = set()        # 就是哈希表，只能放不一样的字符
start = 0
temp = 0
for i in range(len(s)):
    temp += 1
    while s[i] in nums:
        nums.remove(s[start])       # 从头开始减
        start += 1
        temp -= 1
    if temp > ans:
        ans = temp
    nums.add(s[i])      #  如果加在开头就把自己也删了，不，是根本加不进去

print(ans)

#   发现这些都是空间换时间
