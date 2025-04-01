# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_ = max(arr) 
        print(len(arr))
        max_ind = {}
        for i in range(len(arr)):
            if arr[i] == max_:
                max_ind[max_] = i
        print(max_ind)
        if max_ind[max_] == 0:
            return False
        print(len(arr) - max_ind[max_])
        if len(arr) - max_ind[max_] == 1:
            return False

        for i in range(max_ind[max_], len(arr)-1):
            if arr[i+1] >= arr[i]:
                return False
        for i in range(0 ,max_ind[max_]):
            if arr[i] >= arr[i+1]:
                return False
        
        return True