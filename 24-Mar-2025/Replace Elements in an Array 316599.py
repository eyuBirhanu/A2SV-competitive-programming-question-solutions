# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idxTrack = {}
        for i in range(len(nums)):
            idxTrack[nums[i]] = i
        for x, y in operations:
            if x in idxTrack:
                index = idxTrack[x]
                nums[index] = y
                del idxTrack[x]
                idxTrack[y] = index
        return nums
            
       