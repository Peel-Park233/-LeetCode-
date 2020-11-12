root = 10
white, gray =0, 1
stack = [(white, root), (gray, root)]
# stack[0][0] = 99    # 元祖里面的数不能改变
print(stack)
color, node = stack.pop()
print(color, node)
print(stack)
A = ' 42'
print( A[0])