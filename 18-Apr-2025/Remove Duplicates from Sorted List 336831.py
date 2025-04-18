# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return head
        curr = head
        fast = head.next
        while fast:
            if fast.val == curr.val:
                while fast and fast.val == curr.val:
                    fast = fast.next 
                curr.next = fast
            else:
                curr = curr.next
                fast = fast.next
        return head