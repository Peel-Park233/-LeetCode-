#  题目描述：
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

class Solution:
    def restoreIpAddresses(self, s):
        # 定义查找符合条件的数字个数
        num = 4

        #   start 开始的节点，path目前的路径比如（255， 25）
        def _dfs(start, path):      # 每次递归循环就是确定path中一个位置如255
            #   定义结束的条件， 最后一个长度大于num或者地址长度够了，但是指针没指向结尾
            if len(path) > num or (len(path) == num and start < len(s) - 1):
                return  # 这条路走不通，这部分递归就结束了
            if start == len(s): # 指针指向最后的长度,因为是位置所以比len大于1
                print(start - len(s))
                if len(path) == num:
                    # ans.append('.'.join(path))
                    ans.append('.'.join(path))
                return  # 将这个结果加入ans,这条路也到头了

            if s[start] == '0':
                path.append(s[start])
                _dfs(start+1, path)
                path.pop()  # 删除path最末尾那个
                return
            #   递归查找，初始点到最后
            for i in range(start, len(s)):
                if 0 <= int(s[start: i+1]) <= 255:
                    path.append(s[start: i+1])    # 将这个值加入path中
                    print(path)
                    _dfs(i+1, path)
# 删除最后一个数，就是说，如果上面那个递归return后，最后一个节点删除了继续for循环换个新的，就是各条路一起走
                    path.pop()
                else:
                    break
            return
        ans = []
        _dfs(0, [])
        return ans


s = "25525511135"
print(Solution().restoreIpAddresses(s))
#   思路：一个两个三个地去找，如果最后得到的结果都在0到255之间，那么append这个结果
#   DFS深度优先搜索按照深度优先的方式进行搜索，通俗来说就是"一条路走到黑"。
#   就是优先搜索精度
