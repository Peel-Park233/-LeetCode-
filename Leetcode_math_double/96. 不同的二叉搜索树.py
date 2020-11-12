# 题目描述:
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

#   突然想起来怎么做了，分治的思想，几乎都会用到。如果n是14，head是7，左边6的和，右边7的和
#   用数学公式表示


class Solution:
    def numTrees(self, n):
        func = [0 for _ in range(n + 1)]
        func[0] = 1
        func[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                # print('j=' + str(j))
                # print('i=' + str(i))
                # print(i)
                # print(func[i])
                func[i] += func[j] * func[i - j -1]
        return func[-1]


if __name__ == '__main__':
    n = 3
    print(Solution().numTrees(n))


#   要点：还是要看清楚最后要输出的是什么
#   化为公式去求



