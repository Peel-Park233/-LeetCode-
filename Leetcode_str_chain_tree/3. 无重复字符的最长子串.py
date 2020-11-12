s = 'abcabcbb'
#   如何遍历，就是遍历起始点的位置
ans = 0
for i in range(len(s)):
    temp = 1
    temp_nums = set()
    temp_nums.add(s[i])
    for j in range(i+1, len(s)):
        if s[j] not in temp_nums:
            temp += 1
            temp_nums.add(s[j])
        else:
            break
    # print(temp)
    # print(temp_nums)
    ans = max(ans, temp)

print(ans)

#   还是那个道理，先想着如何遍历，原来set就是哈希表
