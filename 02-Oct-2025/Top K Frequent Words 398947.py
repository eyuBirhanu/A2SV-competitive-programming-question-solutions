# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        colle = [] 
        for key, value in count.items():
            colle.append((-value, key))
        
        heapq.heapify(colle)
        
        res = []
        i = 0 
        while i < k:
            res.append(heapq.heappop(colle)[1])
            i += 1
        return res