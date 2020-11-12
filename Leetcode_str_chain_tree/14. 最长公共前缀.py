class Solution:
    def longestCommonPrefix(self, strs):
        ans = ''
        if not strs or strs ==[""]:
            return ""
        if len(strs) == 1:
            return strs[0]
        #   按长短给他冒泡排序吧
        for k in range(len(strs) - 1):
            for l in range(len(strs) - k - 1):
                if len(strs[l]) > len(strs[l+1]):
                    strs[l], strs[l+1] = strs[l+1], strs[l]
        for j in range(len(strs[0])):
            for i in strs:
                if strs[0][j] != i[j]:
                    return ans
            ans += strs[0][j]

        return ans

strs = ["flower", "flow", "flight"]
strs.sort() #   这里sort排序方法好像有点不一哟，好像是按照字母排序的
print(strs)
# strs = ["", "b"]
print(Solution().longestCommonPrefix(strs))

#   free bug 我起飞啦

#   先找出数组中字典序最小和最大的字符串，最长公共前缀即为这两个字符串的公共前缀
#   就是直接sort一下然后比较第一个和最后一个的相似度