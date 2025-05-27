# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        res = {}
        l = 0
        r = sum(nums)
        res[r] = [0]
        i = 0
        for n in nums:
            i += 1
            if n == 0:
                l += 1
            else:
                r -= 1
            sum_ = l + r
            if sum_ in res:
                res[sum_].append(i)   
            else:
                maxInRes = max(res.keys())
                if sum_ > maxInRes:
                    res = {}
                    res[sum_] = [i]
        for _ ,r in res.items():
            return r

        