# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        pref = [0] * (len(self.nums)+1)
        
        for i in range(len(self.nums)):
            pref[i+1] = pref[i] + self.nums[i]
        return pref[right+1] - pref[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)