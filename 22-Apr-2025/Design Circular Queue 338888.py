# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.arr = []

    def enQueue(self, value: int) -> bool:
        if len(self.arr) == self.k:
            return False
        self.arr.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.arr) == 0:
            return False
        self.arr.pop(0)
        return True

    def Front(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr[0]
        

    def Rear(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr[-1]

    def isEmpty(self) -> bool:
        if len(self.arr) == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if len(self.arr) == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()