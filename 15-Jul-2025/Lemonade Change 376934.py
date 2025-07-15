# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5 = 0
        cnt10 = 0
        for b in bills:
            if b == 5:
                cnt5 += 1
            elif b == 10:
                cnt10 += 1
            
            if b == 10:
                if cnt5 < 1:
                    return False
                cnt5 -= 1
            
            if b == 20:
                if cnt10 < 1 and cnt5 < 1:
                    return False

                elif cnt10 < 1:
                    if cnt5 > 2:
                        cnt5 -= 3
                    else:
                        return False

                elif cnt10 > 0 and cnt5 > 0:
                    cnt10 -= 1
                    cnt5 -= 1
                else:
                    return False
        return True
                    
                
