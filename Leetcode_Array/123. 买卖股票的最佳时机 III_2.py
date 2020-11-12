class Solution:
    def maxProfit(self, prices) -> int:
        buy_1 = buy_2 = float('inf')  # 第一二次买之前的最低价
        pro_1 = pro_2 = 0
        #   就是维护两个变量咯，买的时候选最低的买
        for p in prices:
            buy_1 = min(buy_1, p)       # 只有股票降价了才会选这个
            pro_1 = max(pro_1, p - buy_1)   # 只有股票升值了才会选这个

            buy_2 = min(buy_2, p - pro_1)  # p - pro_1 是用第一次的钱抵消了一部分第二次买的钱
            print(buy_2)
            pro_2 = max(pro_2, p - buy_2)
        # print(buy_1, buy_2, pro_1, pro_2)
        return pro_2


prices = [2, 4, 5, 7, 1, 8]
Solution().maxProfit(prices)
