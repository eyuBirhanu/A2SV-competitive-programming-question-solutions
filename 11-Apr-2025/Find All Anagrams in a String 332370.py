# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_cnt = Counter(p)
        s_init = s[:len(p)]
        s_cnt = Counter(s_init)
        if p_cnt == s_cnt:
            res.append(0)  
        j = 0
        for i in range(len(p), len(s)):
            if s[i] not in s_cnt:
                s_cnt[s[i]] = 1
            else:
                s_cnt[s[i]] += 1
            s_cnt[s[j]] -= 1
            if s_cnt[s[j]] == 0:
                del s_cnt[s[j]]
            j += 1
            if s_cnt == p_cnt:
                res.append(i-len(p)+1) 
        return res
            