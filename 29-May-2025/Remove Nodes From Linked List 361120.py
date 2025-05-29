# Problem: Remove Nodes From Linked List - https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=problem-list-v2&envId=recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            if not arr:
                arr.append(curr.val)
                curr = curr.next
                continue
            while arr and arr[-1] < curr.val:
                arr.pop()
            arr.append(curr.val)
            curr = curr.next
        
        dummy = ListNode(0)
        dPtr = dummy
        for n in arr:
            newNode = ListNode(n) 
            dPtr.next = newNode
            dPtr = dPtr.next
        return dummy.next
