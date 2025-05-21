# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        oLen = len(nums)
        nums += nums
        store = [0]
        res = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            while store and nums[i] > nums[store[-1]]:
                index = store.pop()
                res[index] = nums[i]
            store.append(i)
            
        return res[:oLen]