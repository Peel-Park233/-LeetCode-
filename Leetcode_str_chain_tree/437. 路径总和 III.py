class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        result = []

        def add_result(root, result, sum):  # 1.1确定递归函数的参数1.此时的根节点，2.上一层可能的数据
            # 2.确定终止条件：就是下面没有节点了
            if not root:
                return 0
            # 3.确定单层递归的逻辑： 确定每一层递归需要处理的信息。就是这层所有可能的值，加上自己。和sum比较是否一样
            result = [root.value + num for num in result]
            result.append(root.val)
            count = 0
            for k in result:
                if k == sum:
                    count += 1
                    #   1.2确定返回值，就是这一层为止所有可能的count，加上这一层右节点所有可能的count,加上这一层左节点所有可能的count
            return count + add_result(root.left, result, sum) + add_result(root.right, result, sum)
        return add_result(root, result, sum)

