# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        res = 0
        for key, value in cnt.items():
            res += ceil(value / (key + 1)) * (key + 1)
        return res