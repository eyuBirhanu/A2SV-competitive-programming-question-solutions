# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        visited.add(0)
        q = deque()
        q.append(rooms[0])

        while q:
            keys = q.popleft()

            for key in keys:
                if key not in visited:
                    q.append(rooms[key]) 
                    visited.add(key)
        return len(rooms) == len(visited)