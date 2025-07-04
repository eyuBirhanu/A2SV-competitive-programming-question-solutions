# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for li in lists:
            curr = li
            while curr:
                arr.append(curr.val)
                curr = curr.next
        arr.sort()
        res = ListNode(0)
        res_ptr = res
        for i in arr:
            NewNode = ListNode(i)
            res_ptr.next = NewNode
            res_ptr = res_ptr.next
        return res.next