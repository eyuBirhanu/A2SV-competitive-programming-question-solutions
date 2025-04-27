# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxtGR = defaultdict(lambda: -1)
        store = []
        for num in nums2:
            if not store:
                store.append(num)
            else:
                if num < store[-1]:
                    store.append(num)
                else:
                    nxtGR[store[-1]] = num
                    store.pop()
                    store.append(num)

                    while len(store) > 1 and store[-1] > store[-2]:
                        nxtGR[store[-2]] = store[-1]
                        store.pop(-2)
        res = []
        for num in nums1:
            res.append(nxtGR[num])
        return res