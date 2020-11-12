class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int):
        ans = []
        edges = flights
        def findway(temp, number, rmb):
            if number < 0:
                return
            if temp == dst:
                ans.append(rmb)
                return
            for i in range(len(edges)):
                if edges[i][0] == temp:
                    findway(edges[i][1], number-1, rmb+edges[i][2])
        #   遍历所有的起点
        number = K
        for i in range(len(edges)):
            if edges[i][0] == src:
                findway(edges[i][1], number, edges[i][2])
        return min(ans) if len(ans) > 0 else -1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1
print(Solution().findCheapestPrice(n, flights, src, dst, K))

#   超时！！！！