# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        arr = []
        read = 0
        step = 0
        while read < len(processorTime):
            i = 0
            while i < 4:
                num = processorTime[read] + tasks[step]
                arr.append(num)
                step += 1
                i += 1
            read += 1
        return max(arr)
                