#   题目描述：214. 最短回文串
#  给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。
#  找到并返回可以用这种方式转换的最短回文串。


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        ss = s[::-1]
        length = len(s)
        for i in range(length):
            if ss[i:] == s[:length - i]:
                return ss[:i] + s
        return ss + s

#   要点：对字符串的操作可以是几个一起比较
