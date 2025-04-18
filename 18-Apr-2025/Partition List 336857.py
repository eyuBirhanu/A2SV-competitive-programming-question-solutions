# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode()
        larger = ListNode()

        smaller_ptr = smaller
        larger_ptr = larger

        curr = head
        while curr:
            if curr.val < x:
                smaller_ptr.next = curr 
                smaller_ptr = smaller_ptr.next
            else:
                larger_ptr.next = curr 
                larger_ptr = larger_ptr.next
            curr = curr.next
        larger_ptr.next = None
        smaller_ptr.next = larger.next
        return smaller.next