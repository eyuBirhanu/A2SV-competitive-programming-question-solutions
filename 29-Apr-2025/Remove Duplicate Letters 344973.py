# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # s
        cnt = Counter(s) 
        seen = set()
        res = []
        for c in s:
            if not res:
                res.append(c)
                seen.add(c)
            else:
                if c in seen:
                    cnt[c] -= 1
                    continue
                else:
                    while res and c < res[-1] and cnt[res[-1]] > 0:
                        seen.remove(res[-1])
                        res.pop()
                    res.append(c)
                    seen.add(c)
            cnt[c] -= 1
        return ''.join(res)