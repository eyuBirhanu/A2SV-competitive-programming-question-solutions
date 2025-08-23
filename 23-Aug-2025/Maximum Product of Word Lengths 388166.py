# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        # fsr
        def id_disjoint(s1, s2):
            return set(s1).isdisjoint(set(s2))
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if id_disjoint(words[i], words[j]):
                    product = len(words[i]) * len(words[j])
                    max_product = max(product, max_product)
        return max_product