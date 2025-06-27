# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(i, used, sub):
            if i == len(nums):
                ans.append(sub[:])
                return
            for j in range(len(nums)):
                if j in used or (j > 0 and nums[j] == nums[j-1] and j-1 not in used):
                    continue
                sub.append(nums[j])
                used.add(j)
                dfs(i+1, used, sub)
                sub.pop()
                used.remove(j)

        dfs(0, set(), [])
        return ans