# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = {node: float('inf') for node in range(1, n+1)}

        distances[k] = 0

        processed = set() 

        heap = [(0, k)]

        while heap:
            curr_dist , curr_node = heapq.heappop(heap)
            if curr_node in processed:
                continue
            
            processed.add(curr_node)

            for child, weight in graph[curr_node]:
                distance = curr_dist + weight
                if distance < distances[child]:
                    distances[child] = distance
                    heapq.heappush(heap, (distance, child))

        res = distances.values()
        if float('inf') in res:
            return -1
        return max(res)