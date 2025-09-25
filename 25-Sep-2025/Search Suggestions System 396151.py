# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []

        for i in range(len(searchWord)):
            let = searchWord[:i+1]
            sub = []
            for word in products:
                if word.startswith(let):
                    sub.append(word)
            sub.sort()
            if len(sub) > 3:
                res.append(sub[:3])
            else:
                res.append(sub)
        return res
