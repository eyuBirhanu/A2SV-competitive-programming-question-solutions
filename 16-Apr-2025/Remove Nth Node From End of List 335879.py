# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        fast = 0
        while curr and fast < n:
            curr = curr.next
            fast += 1
        slow = dummy
        while curr:
            slow = slow.next
            curr = curr.next
        slow.next = slow.next.next
        return dummy.next