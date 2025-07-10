# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        l, r = 0, len(self.arr)-1
        mid = (l+r) // 2
        if r % 2 == 1:
            return (self.arr[mid] + self.arr[mid+1] ) / 2
        return self.arr[mid]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()