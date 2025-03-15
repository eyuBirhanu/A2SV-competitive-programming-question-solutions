# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] > k:
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] == k:
                cnt += 1
                i += 1
                j -= 1
        return cnt