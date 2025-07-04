# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, l2):
            res = []
            while l1 and l2:
                if l1[0] > l2[0]:
                    res.append(l2[0])
                    l2.pop(0)
                else:
                    res.append(l1[0])
                    l1.pop(0)
            
            while l1:
                res.append(l1[0])
                l1.pop(0)
            while l2:
                res.append(l2[0])
                l2.pop(0)
            
            return res


            
        if len(nums) == 1:
            return nums
        
        arr1 = nums[: len(nums)//2]
        arr2 = nums[(len(nums)//2):]

        arr1 = self.sortArray(arr1)
        arr2 = self.sortArray(arr2)

        return merge(arr1, arr2)