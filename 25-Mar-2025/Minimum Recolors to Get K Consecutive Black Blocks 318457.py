# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        w_cnt = {'W':0} 
        for i in window:
            if i == 'W':
                w_cnt['W'] += 1
        min_op = w_cnt['W']
        j = 1
        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W' and w_cnt['W'] > 0:
                w_cnt['W'] -= 1
            
            if blocks[i] == 'W':
                w_cnt['W'] += 1
            min_op = min(min_op, w_cnt['W'])

            j += 1
        print(len(blocks))
        return min_op
