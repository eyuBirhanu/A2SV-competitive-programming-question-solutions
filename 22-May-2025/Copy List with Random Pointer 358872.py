# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        listSet = { None : None }
        curr = head
        while curr:
            newNode = Node(curr.val)
            listSet[curr] = newNode
            curr = curr.next
        
        curr = head

        while curr:
            copy = listSet[curr]
            copy.next = listSet[curr.next]
            copy.random = listSet[curr.random]
            curr = curr.next
        return listSet[head]
        