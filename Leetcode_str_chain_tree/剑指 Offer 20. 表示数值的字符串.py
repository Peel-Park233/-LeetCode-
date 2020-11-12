class Solution:
    def isNumber(self, s: str) -> bool:
        try:
             float(s)
        except ValueError:
            return False
        return True

# 妙啊。。。
