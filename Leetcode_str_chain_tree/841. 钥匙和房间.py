#   一看就是链表，其实用递归做啦
class Solution:
    def canVisitAllRooms(self, rooms):
        A = set()
        M = []  # 记录已经搜索过的房间号
        #   k代表搜索的房间号
        A.add(0)
        def check_room(rooms, k):
            for i in rooms[k]:
                A.add(i)
                if i not in M:
                    M.append(i)
                    check_room(rooms, i)

        check_room(rooms, 0)
        print(A)
        if len(A) == len(rooms):
            return True
        else:
            return False


# rooms = [[1], [2], [3], []]
rooms = [[1, 3], [3, 0, 1], [2], [0]]

print(Solution().canVisitAllRooms(rooms))


