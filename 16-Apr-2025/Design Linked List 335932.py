# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None  

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr and i <= index:
            if index == i:
                return curr.data
            curr = curr.next
            i += 1 
            
        else:
            return -1 

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        newNode.next = curr
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        if curr is None:
            self.head = newNode
            return
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        if curr is None:
            return
        
        for i in range(index-1):
            if curr is None:
                return
            curr = curr.next
        if curr is None:
            return 
        nxt = curr.next
        curr.next = newNode
        newNode.next = nxt 

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if index == 0 and self.head is not None:
            self.head = self.head.next
            return
        
        for i in range(index-1):
            curr = curr.next
        if curr is None or curr.next is None:
            return 
        curr.next = curr.next.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)