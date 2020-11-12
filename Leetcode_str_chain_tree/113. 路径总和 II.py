class Solution:
    def pathSum(self, root, sum_1: int):
        ans = []
        if not root:
            return ans
        def dfs(root, temp):
            if not root:
                return
            # print(temp)
            if sum(temp) == sum_1 and not root.left and not root.right:
                ans.append(temp)
                return
            if root.right:
                dfs(root.right, temp + [root.right.val])
            if root.left:
                dfs(root.left, temp + [root.left.val])
        dfs(root, [root.val])
        return ans


#   套路来咯，输入值，返回值，出口，单层逻辑。
#  老DFS了


