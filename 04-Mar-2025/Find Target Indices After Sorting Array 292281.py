# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target_index = []
        len_ = len(nums)
        # using bubble sort
        for k in range(len_):
            for i in range(len_ - k -1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        for i in range(len(nums)):
            if nums[i] == target:
                target_index.append(i)
        return target_index