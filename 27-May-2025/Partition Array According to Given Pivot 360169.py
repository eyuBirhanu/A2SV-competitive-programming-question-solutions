# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        equal = []
        for n in nums:
            if n == pivot:
                equal.append(n)
            elif n < pivot:
                left.append(n)
            else:
                right.append(n) 
        return left + equal + right
        