class Solution:
    # 计算以当前节点为根的树深度,这个可以记录作为模板，就是查找二叉树最深的深度
    def Depth(self, root):
        if root:
            return 1 + max(self.Depth(root.left), self.Depth(root.right))
        return 0

    def isBalanced(self, root):  # 1.确定递归函数的参数
        # 空树是AVL
        if not root:
            return True   # 结束的点，说明这个确实会执行很多次，关键是最后有个and，只要有一个false就不行
        # 若左右子树深度超过1，非AVL
        if abs(self.Depth(root.left) - self.Depth(root.right)) > 1:  # 每一步就是判断左边和右边的最深深度
            return False
        # 递归执行，当出现不满足AVL性质的子树时，执行短路运算立即返回结果
        return self.isBalanced(root.left) and self.isBalanced(root.right)
A = 1
if A==1:
    print('yes')
else:
    print('no')

