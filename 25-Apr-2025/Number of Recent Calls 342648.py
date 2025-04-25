# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.cnt = 0
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.cnt += 1

        while self.queue[0] not in range((self.queue[-1] - 3000) , self.queue[-1]+1):
            self.queue.popleft()
            self.cnt -= 1
            # s
        return self.cnt

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)