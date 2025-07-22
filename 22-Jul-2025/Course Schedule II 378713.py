# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        
        res = []
        q = deque()
        for course in range(numCourses):
            if incoming[course] == 0:
                q.append(course)

        while q:
            course = q.popleft()
            res.append(course)
            

            for ne in graph[course]:
                incoming[ne] -= 1
                if incoming[ne] == 0:
                    q.append(ne)

        if len(res) != numCourses:
            return []
        return res