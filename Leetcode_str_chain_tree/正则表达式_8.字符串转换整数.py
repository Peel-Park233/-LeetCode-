#   正则表达式，太方便了吧
class Solution:
    def myAtoi(self, str):
        import re
        mathes = re.match('[ ]*([+-]?\d+)', str)
        if not mathes:
            return 0
        ans = int(mathes.group(1))
        return min(max(ans, -2**31), 2**31-1)
str = ' -1231241das'
print(Solution().myAtoi(str))


#   正则表达式太好用了吧，只要规定是这种类型就好了
#   第一步从简单的例子来看，看看有没有规律