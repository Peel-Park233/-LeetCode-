class Solution:
    def convertBST(self, root):
        #   中序遍历有点像，左中右,现在要反向中序遍历，右左中
        self.total = 0
        def mid_dfs(root):
            if not root:
                return
            mid_dfs(root.right)     # 这样深度优先不断往他的右边跑
            self.total += root.val  # 应该是这个操作还没掌握，一直记录一个和，然后把这个和复制给这个节点
            root.val = self.total
            mid_dfs(root.left)
        mid_dfs(root)
        return root