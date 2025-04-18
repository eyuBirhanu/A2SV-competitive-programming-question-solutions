# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head is None:
            return head
        current = head
        cnt = 0

        while current:
            cnt += 1
            current = current.next
        k %= cnt

        pref = ListNode()
        suff = ListNode()

        pref_ptr = pref
        suff_ptr = suff
        curr = head

        check = 0
        while curr:
            if check < (cnt-k):
                suff_ptr.next = curr
                suff_ptr = suff_ptr.next
                check += 1
            else:
                pref_ptr.next = curr
                pref_ptr = pref_ptr.next
            curr = curr.next

        suff_ptr.next = None
        pref_ptr.next = suff.next
        return pref.next
