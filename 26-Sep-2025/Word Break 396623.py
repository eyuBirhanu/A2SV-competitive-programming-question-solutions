# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def bt(word):
            if word in wordDict:
                return True

            if word in memo:
                # eterrteyty
                return memo[word]
            
            memo[word] = False

            for wo in wordDict:
                if word.startswith(wo):
                    memo[word] = memo[word] or bt(word[len(wo):])

            return memo[word]
        
        return bt(s)