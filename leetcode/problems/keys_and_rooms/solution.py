class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        unlocked = set()
        unlocked.add(0)
        queue = deque([rooms[0]])

        while(queue):
            if len(unlocked) == n: return True
            room = queue.popleft()
            for key in room:
                if key not in unlocked:
                    unlocked.add(key)
                    queue.append(rooms[key])

        return len(unlocked) == n