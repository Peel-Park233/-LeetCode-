class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31 -1 or x < -2**31:
            return 0
        x = str(x)
        if len(x) <= 1:
            return int(x)
        temp = 0
        if x[0] == '-':
            x = x[1:]
            temp = 1
        while x[-1] == '0':
              x = x[:-1]        # 字符串删除最后一个数，因为左闭右开-1是取不到的
        if temp == 0:
            return int(x[::-1]) if int(x[::-1]) < 2**31 -1 else 0
        else:
            return - int(x[::-1]) if -int(x[::-1]) > -2**31 else 0


x = -120
print(Solution().reverse(x))
#   容易嘛，一题简单题错了10次