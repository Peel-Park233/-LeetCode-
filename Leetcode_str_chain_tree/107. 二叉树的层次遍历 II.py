# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        #   深度优先搜索dfs
        if not root:
            return []
        ans = []
        def dfs(root, level):
            if level + 1 > len(ans):    # 因为level是从0层开始的
                ans.append([])
            ans[level].append(root.val)
            if not root.left and not root.right:
                return
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)
        dfs(root, 0)
        ans = ans[::-1]

        return ans

root = TreeNode[3, 9, 20, None, None, 15, 7]
print(Solution().levelOrderBottom(root))