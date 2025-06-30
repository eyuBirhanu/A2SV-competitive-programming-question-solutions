# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = [] 
        def dfs(i, vals, sum_):
            if sum_ == target:
                ans.append(vals.copy())
                return
            if sum_ > target or i >= len(candidates):
                return 
            
            vals.append(candidates[i])
            dfs(i, vals, sum_ + candidates[i])
            vals.pop()
            
            dfs(i+1, vals, sum_)

        dfs(0, [], 0)
        return ans 