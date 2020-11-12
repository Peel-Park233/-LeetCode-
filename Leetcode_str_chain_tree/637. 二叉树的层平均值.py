# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        ans = []

        def dfs(root, level):
            if level > len(ans) - 1:
                ans.append([])
            ans[level].append(root.val)
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        dfs(root, 0)
        final = []
        for i in range(len(ans)):
            final.append(sum(ans[i]) / len(ans[i]))

        return final