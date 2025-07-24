# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        inDegree = defaultdict(int)
        graph = defaultdict(list)

        res = [x for x in range(len(quiet))]

        for rich , poor in richer:
            graph[rich].append(poor)
            inDegree[poor] += 1
        
        q = deque()
        
        for i in range(len(quiet)):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            ele = q.popleft() 
            for e in graph[ele]:
                inDegree[e] -= 1
                if quiet[res[e]] > quiet[res[ele]]:
                    res[e] = res[ele]
                if inDegree[e] == 0:
                    q.append(e)
        return res