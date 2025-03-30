# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = arr.copy()
        i = 0 
        j = 0
        while i < len(arr) and j < len(arr):
            if new_arr[i] == 0:
                if j < len(arr):
                    arr[j] = 0
                    j += 1
                if j < len(arr):
                    arr[j] = 0
                    j += 1
            else:
                arr[j] = new_arr[i]
                j += 1
            i += 1 