# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        max_ = float('-inf')
        maxCount = 0
        trees = {}
        j = 0
        for i in range(len(fruits)):
            while len(trees) > 2:
                trees[fruits[j]] -= 1
                if trees[fruits[j]] == 0:
                    del trees[fruits[j]]
                j += 1 
                maxCount -= 1
            if fruits[i] in trees:
                trees[fruits[i]] += 1
            else:
                trees[fruits[i]] = 1
            maxCount += 1

            if len(trees) == 2:
                max_ = max(maxCount, max_)
        if len(trees) <= 2 and maxCount > 0:
            max_ = max(maxCount, max_)
        return max_