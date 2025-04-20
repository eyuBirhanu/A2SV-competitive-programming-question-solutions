# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left == 0:
            return head
        left -= 1
        right -= 1
        start_prev  = None
        end_next = None
        start = None
        end = None
        curr = head
        prev = None
        cnt = 0
        while curr:
            if cnt == right+1:
                end_next = curr 

            if cnt == left-1:
                start_prev = curr

            if cnt >= left and cnt <= right:
                if cnt == left:
                    end = curr
                if cnt == right:
                    start = curr
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            else:
                curr = curr.next

            cnt += 1
        
        if start_prev:
            start_prev.next = start
        else:
            head = start
        end.next = end_next
        return head
        