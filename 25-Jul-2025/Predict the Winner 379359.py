# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recursive(l, r, p1, p2, turn):
            if l > r:
                return p1 >= p2
            
            if turn == 1:
                fir = recursive(l+1, r, p1+nums[l], p2, 2)
                sec = recursive(l, r-1, p1+nums[r], p2, 2)
                return fir or sec
            else:
                fir = recursive(l+1, r, p1, p2+nums[l], 1)
                sec = recursive(l, r-1, p1, p2+nums[r], 1)
                return fir and sec
            
        return recursive(0, len(nums)-1, 0, 0, 1)