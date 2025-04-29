# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.k = k
        self.cnt = 0

    def insertFront(self, value: int) -> bool:
        if self.cnt < self.k:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.cnt += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.cnt < self.k:
            node = Node(value)
            if not self.head:
                self.head = node
            else:
                curr = self.head
                while curr.next:
                    curr = curr.next
                curr.next = node
            self.cnt += 1
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        self.head = self.head.next
        self.cnt -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.head:
            return False
        if self.head.next is None:
            self.head = None
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None

        self.cnt -= 1
        return True

    def getFront(self) -> int:
        if not self.head:
            return -1
        return self.head.val
        

    def getRear(self) -> int:
        if not self.head:
            return -1
        curr = self.head 
        while curr.next:
            curr = curr.next
        return curr.val
        

    def isEmpty(self) -> bool:
        if self.cnt == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.cnt == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()