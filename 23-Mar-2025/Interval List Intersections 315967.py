# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i ,j = 0, 0
        ans = []
        start, end = 0, 1
        while i < len(firstList) and j < len(secondList):
            if secondList[j][end] < firstList[i][start]:
                j += 1
                continue
            elif firstList[i][end] < secondList[j][start]:
                i += 1
                continue
            
            intersection = []  
            if secondList[j][end] >= firstList[i][start]:
                intersection.append(max(firstList[i][start], secondList[j][start]))
                intersection.append(min(firstList[i][end], secondList[j][end]))
                ans.append(intersection)
            

            if j < len(secondList)-1 and firstList[i][end] >= secondList[j+1][start] and firstList[i][end] >= secondList[j+1][end]:
                j += 1
                continue
            if i < len(firstList)-1 and secondList[j][end] >= firstList[i+1][start] and secondList[j][end] >= firstList[i+1][end]:
                i += 1
                continue
            
            
            
            intr = []
            if  j < len(secondList)-1 and firstList[i][end] >= secondList[j+1][start]:
                intr.append(min(firstList[i][end], secondList[j+1][start]))
                intr.append(max(firstList[i][end], secondList[j+1][start]))
                ans.append(intr)
            elif i < len(firstList)-1 and secondList[j][end] >= firstList[i+1][start]:
                intr.append(min(secondList[j][end], firstList[i+1][start]))
                intr.append(max(secondList[j][end], firstList[i+1][start]))
                ans.append(intr)
           
            i += 1
            j += 1
        return ans
