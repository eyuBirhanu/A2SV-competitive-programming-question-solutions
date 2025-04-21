# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # s
        cnt = 0
        current = head
        while current:
            cnt += 1
            current = current.next
        itere = cnt // 2

        curr = head
        reverse = None

        while curr:
            newNode = ListNode(curr.val)
            newNode.next = reverse
            reverse = newNode
            curr = curr.next
        max_sum = float('-inf')
        
        head_ptr = head
        reverse_ptr = reverse

        while head_ptr and reverse_ptr and itere > 0:
            sum_ = head_ptr.val + reverse_ptr.val
            max_sum = max(max_sum,  sum_) 
            head_ptr = head_ptr.next
            reverse_ptr = reverse_ptr.next
            itere -= 1
        return max_sum
