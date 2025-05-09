# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        if letters[-1] <= target:
            return letters[0]
        res = ''
        while l <= r:
            mid = (l+r)//2
            if letters[mid] > target:
                res = letters[mid]
                r = mid -1
            else:
                l = mid +1
        return res
            
        