# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            a = nums[i]
            j = i + 1
            k = len(nums) -1 
            while j < k:
                if nums[j] + nums[k] + a == 0:
                    ans.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1 
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                
                elif nums[j] + nums[k] + a < 0:
                    j += 1
                else:
                    k -= 1
        return ans