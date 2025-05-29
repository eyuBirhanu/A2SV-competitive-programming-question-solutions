# Problem: Increasing Triplet Subsequence - https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_ = float('inf')
        max_ = float('-inf')
        for n in nums:
            if min_ != float('inf') and max_ != float('-inf'):
                if n > max_:
                    return True
            if n < min_:
                min_ = n
            elif n > min_:
                max_= n
        return False
        