# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        chars = defaultdict(list)

        for c in range(len(s)):
            chars[s[c]].append(c)

        res = 0

        for word in words:
            curr = -1
            isThere = True

            for c in word:
                if c in chars:
                    next_pos = bisect_left(chars[c], curr + 1)

                    if next_pos < len(chars[c]):
                        curr = chars[c][next_pos]
                    else:
                        isThere = False
                else:
                    break
                if isThere == False:
                    break
            else:
                res += 1
        return res
