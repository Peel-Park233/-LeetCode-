class Solution:
    def multiply(self, num1: str, num2: str) -> str:    # 这样可以规划输入输出格式吗
        # number_1 = int(num1)
        # number_2 = int(num2)
        # return str(number_1 * number_2)
        #  秒解  - -
        num1 = num1[::-1]
        num2 = num2[::-1]
        number_1 = 0
        number_2 = 0
        for i in range(len(num1)):
            number_1 += 10 ** i * int(num1[i])
        for i in range(len(num2)):
            number_2 += 10 ** i * int(num2[i])
        return str(number_1 * number_2)

num1 = '123'
num2 = '456'
print(Solution().multiply(num1, num2))