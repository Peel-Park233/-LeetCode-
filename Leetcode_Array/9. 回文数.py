class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        temp = x[::-1]      # x随着temp一起变？？不是，字符串不会一起变，数字也不会一起变
        # temp.append(1)      # 如果是列表，就会一起变！！！！
        return True if x == temp else False




x = 123125412
# x = [1, 23, 123, 412]
print(Solution().isPalindrome(x))
