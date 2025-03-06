# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        missed_list = []
        for i in arr1 :
            if i not in arr2 :
                missed_list.append(i) 
        for i in range(len(arr2)):
            count = 0
            for j in arr1:
                if j == arr2[i]:
                    count += 1
            arr2[i] = [arr2[i], count]
        final = []
        print(arr2)
        for i in range(len(arr2)):
            for j in range(arr2[i][1]):
                final.append(arr2[i][0])
        return final + sorted(missed_list)