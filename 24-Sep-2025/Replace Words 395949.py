# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        
        ans = []
        
        for word in sentence:
            res = word
            for w in dictionary:
                if word.startswith(w) and len(w) < len(res):
                    res = w
            ans.append(res)
        return ' '.join(ans)
            