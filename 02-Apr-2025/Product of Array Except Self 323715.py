# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        if cnt[0] > 1:
            nums = [0] * len(nums)
        elif cnt[0] == 1:
            ind_map = {}
            mul = 1 
            for i in range(len(nums)):
                ind_map[nums[i]] = i
                if nums[i] != 0:
                    mul *= nums[i]
            for i in range(len(nums)):
                if i == ind_map[0]:
                    nums[i] = mul
                else:
                    nums[i] = 0
        else:
            mul = 1
            for i in range(len(nums)):
                mul *= nums[i]
            for i in range(len(nums)):
                nums[i] = mul//nums[i]
        return nums
