# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for i in range(len(logs)):
            if logs[i] == '../' and cnt > 0:
                cnt -= 1
            elif logs[i] == '../' and cnt == 0:
                cnt = cnt 
            elif logs[i] == './':
                cnt = cnt
            else:
                cnt += 1
        return cnt

        