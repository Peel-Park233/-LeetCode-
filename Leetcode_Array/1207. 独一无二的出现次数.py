class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        arr.sort()
        arr = arr + [2*31-1]    # 在后面填充一个数
        # print(arr)
        ans = []
        temp = 1
        for i in range(1, len(arr)):
            # print(arr[i], arr[i-1], temp)
            if arr[i] == arr[i-1]:
                temp += 1
                # print(temp)
            else:
                # print(temp)
                if temp in ans:
                    return False
                else:
                    ans.append(temp)
                    temp = 1
        # print(ans)
        return True


# 重点！！！无法解决开头或者末尾的问题，可以通过再开头或者末尾填充一个数

# 用字典的方式

class Solution_2:
    def uniqueOccurrences(self, arr) -> bool:
        ans = {}
        for i in arr:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        set1 = set()
        for j in ans:
            if ans[j] in set1:
                return False
            else:
                set1.add(ans[j])

