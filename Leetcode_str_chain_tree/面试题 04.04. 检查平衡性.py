class Solution:
    def isBalanced(self, root):
        result = []
        depth = 0

        def cal_depth(root, depth):     # 1.确定递归函数的参数
            if not root:
                return 0
            depth += 1  # 每一步就是加一
            if root.left:
                cal_depth(root.left, depth)
            else:
                result.append(depth)  # 2.结束的点，每个循环都要从这里出去
            if root.right:
                cal_depth(root.right, depth)
            else:
                result.append(depth)  # 2.结束的点，每个循环都要从这里出去
        cal_depth(root, depth)
        # print(len(result))
        if len(result) == 0:return True
        if max(result) - min(result) <= 1:
            return True
        else:
            return False