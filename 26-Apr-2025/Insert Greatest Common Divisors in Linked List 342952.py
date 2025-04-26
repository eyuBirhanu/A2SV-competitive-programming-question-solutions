# Problem: Insert Greatest Common Divisors in Linked List - https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcf(n1, n2):
            dividend = max(n1, n2)
            divisor = min(n1, n2)
            rem = 0
            if dividend % divisor == 0:
                return divisor
            else:
                while dividend % divisor > 0:
                    rem = dividend % divisor
                    dividend = divisor
                    divisor = rem
                    if dividend % divisor == 0:
                        return divisor
        if head.next == None:
            return head
        fir = head
        sec = head.next
        while sec:
            new_node = ListNode(gcf(fir.val, sec.val))
            fir.next = new_node
            new_node.next = sec
            fir = fir.next.next
            sec = sec.next
        return head
