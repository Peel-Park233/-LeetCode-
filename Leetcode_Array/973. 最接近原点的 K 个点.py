class Solution:
    def kClosest(self, points, K: int):
        # #  看错题目了
        # temp_max = 2**31 - 1
        # temp_point = []
        # for i in range(len(points)):
        #     point = points[i]
        #     if point[0]**2 + point[1]**2 < temp_max:
        #         temp_max = point[0]**2 + point[1]**2
        #         temp_point = [point]
        #         print(temp_max)
        #     elif point[0]**2 + point[1]**2 == temp_max:
        #         temp_point.append(point)
        #     else:
        #         continue
        # return temp_point
        for i in range(len(points)):
            point = points[i]
            points[i].append(point[0]**2 + point[1]**2)
        points.sort(key=lambda x: (x[2]))
        # print(points)
        ans = []
        for i in range(K):
            temp = points[i]
            temp = temp[:2]
            ans.append(temp)
        return ans
        # 流川枫，流川枫

#   小技巧 python列表先按第一个元素排列，再按第二个元素排列（默认升序）
# array = [(3, 5), (1, 1), (2, 3), (5, 15), (4, 10)]
# array.sort(key=lambda x: (x[0], x[1]))