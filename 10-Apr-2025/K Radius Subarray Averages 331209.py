# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ave = [-1]* len(nums)
        sum_ = 0
        x = (k*2)+1
        if x > len(nums):
            return ave
        y = sum(nums[:x])
        ave[k] = y//x
        
        for i in range(k+1, len(nums)-k):
            y += nums[i+k] - nums[i-k-1]
            ave[i] = y//x
        return ave
            