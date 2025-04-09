# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        mass = sum(people)
        sum_ = 0
        boat = 0
        i = 0
        j = len(people)-1
        while i < j and i < len(people):
            if people[i] == limit:
                boat += 1
                sum_ += people[i]
                i += 1
            elif people[i] < limit:
                limit_ = people[i]
                if limit_ + people[j] > limit:
                    boat += 1
                    sum_ += people[i]
                    i += 1
                elif limit_ + people[j] <= limit:
                    boat += 1
                    sum_ += (people[i] + people[j])
                    i += 1
                    j -= 1
            elif people[i] > limit:
                i += 1
        if sum_ < mass:
            boat += 1
        return boat
                
                    
