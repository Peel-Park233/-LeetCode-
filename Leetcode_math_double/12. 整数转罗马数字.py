class Solution:
    def intToRoman(self, num: int) -> str:
        #   暴力法可以做，但是哈希表更好
        # M_number =  num // 1000
        # D_number = (num % 1000) // 500
        # C_number = (num % 500) // 100
        # L_number = (num % 100) // 50
        # X_number = (num % 50) // 10
        # V_number = (num % 10) // 5
        # ans = ''
        # if 0 < M_number < 4:
        #     for i in range(M_number):
        #         ans += 'M'
        # if 0 < D_number < 4:
        #     for i in range(D_number):
        #         ans += 'D'
        # if C_number == 4: #直接在上面设置CD的数更方便
        #     ans += 'CD'
        #   字典的话前面是标记，后面是dic[key]的值
        dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        ans = ''
        for key in dic:
            #   \ 这个标记可以换行
            number = \
                num // key
            ans += number * dic[key]
            num = num % key
        return ans

num = 1234
print(Solution().intToRoman(num))