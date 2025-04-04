# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0 
        let_cnt = {chr(i): 0 for i in range(65, 91)}
        j = 0
        for i in range(len(s)):
            let_cnt[s[i]] += 1
            max_val = max(let_cnt.values())
            if (i-j+1) - max_val <= k:
                max_len = max(max_len, i-j+1)
            else:
                while j < i and (i-j+1) - max_val > k:
                    let_cnt[s[j]] -= 1
                    j += 1
        return max_len
            
            

            