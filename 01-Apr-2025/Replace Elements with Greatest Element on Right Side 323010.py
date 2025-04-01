# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = -1 
        curr = 0
        for i in range(len(arr))[::-1]:
            curr = arr[i]
            arr[i] = max_
            max_ = max(max_, curr)
        return arr