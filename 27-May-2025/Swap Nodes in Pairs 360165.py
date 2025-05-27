# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        i = 0
        j = 1
        while j < len(arr):
            arr[i], arr[j] = arr[j], arr[i]
            i += 2
            j += 2
        ans = ListNode()
        ansPtr = ans

        i = 0 
        while i < len(arr):
            newNode = ListNode(arr[i])
            ansPtr.next = newNode
            ansPtr = ansPtr.next
            i += 1
        return ans.next

        