class Solution:
    def sumNumbers(self, root) -> int:
        if not root:
            return 0
        #   dfs 深度优先搜索
        ans = []
        def dfs(num, root):
            # if not root:
            #     ans.append(num)
            #     return
            # dfs(num + str(root.val), root.left) # 如果这个节点后面没有节点了，他也走了一个root.left和root.right,所以是两倍，需要改变判断的位置
            # dfs(num + str(root.val), root.right)
            if root.left:
                dfs(num + str(root.left.val), root.left)
            if root.right:
                dfs(num + str(root.right.val), root.right)
            if not root.left and not root.right:
                ans.append(num)
                return
        dfs(str(root.val), root)
        # print(ans)
        ans = [int(ans[i]) for i in range(len(ans))]
        # print(ans)
        return sum(ans)