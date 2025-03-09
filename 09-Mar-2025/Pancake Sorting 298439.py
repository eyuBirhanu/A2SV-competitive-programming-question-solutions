# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        if sorted(arr) == arr:
            return ans
        end = len(arr)
        while end > 0:
            sub_arr = arr[:end]
            max_num = max(sub_arr)
            max_index = sub_arr.index(max_num)
            arr[:max_index+1] = arr[:max_index+1][::-1]
            ans.append(max_index+1)
            arr[:end] = arr[:end][::-1]
            ans.append(end) 
            end -= 1
        return ans
