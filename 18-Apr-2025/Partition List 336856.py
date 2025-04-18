# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        cnt = 0
        while current:
            cnt += 1
            current = current.next
        smaller = ListNode()
        larger = ListNode()

        smaller_ptr = smaller
        larger_ptr = larger

        curr = head
        check = 0
        while curr and check <= cnt:
            if curr.val < x:
                smaller_ptr.next = curr 
                smaller_ptr = smaller_ptr.next
            else:
                larger_ptr.next = curr 
                larger_ptr = larger_ptr.next
            curr = curr.next
            check += 1
        larger_ptr.next = None
        smaller_ptr.next = larger.next
        return smaller.next