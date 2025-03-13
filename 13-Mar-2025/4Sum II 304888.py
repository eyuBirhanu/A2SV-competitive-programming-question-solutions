# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = {}
        ans = 0
        for a in nums1:
            for b in nums2:
                sum_ = a+b
                if sum_ not in cnt:
                    cnt[sum_] = 1
                else:
                    cnt[sum_] += 1
        for a in nums3:
            for b in nums4:
                sum_ = -(a+b)
                if sum_ in cnt:
                    ans += cnt[sum_]
        return ans