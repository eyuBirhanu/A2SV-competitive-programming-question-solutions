# Problem: Reorder List - https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)  
            curr = curr.next
        i = 0
        j = len(arr) -1 
        res = []
        while i < j:
            res.append(arr[i])
            res.append(arr[j])
            i += 1
            j -= 1
        if len(arr) % 2 != 0:
            res.append(arr[i])

        curr = head
        for i in range(1, len(res)):
            node = ListNode(res[i])
            curr.next = node
            curr = curr.next 