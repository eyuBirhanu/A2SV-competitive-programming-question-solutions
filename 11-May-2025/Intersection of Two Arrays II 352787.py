# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        for item, value in count2.items():
            if item in count1:
                min_ = min(value, count1[item])
                for i in range(min_):
                    res.append(item)
        return res
            
        