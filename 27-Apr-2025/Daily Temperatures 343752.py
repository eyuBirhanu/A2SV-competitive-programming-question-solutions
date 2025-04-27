# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))] 
        store = []
        for i in range(len(temperatures)):
            if not store:
                store.append((temperatures[i], i))
            else:
                if temperatures[i] > store[-1][0]:
                    while store and temperatures[i] > store[-1][0]:
                        res[store[-1][1]] = i - store[-1][1]
                        store.pop()
                    store.append((temperatures[i], i))
                else:
                    store.append((temperatures[i], i))
        return res