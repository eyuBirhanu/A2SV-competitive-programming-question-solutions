# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        cnt = 0
        while i < len(players) and j < len(trainers):
            if trainers[j] >= players[i]:
                i += 1
                j += 1
                cnt += 1
            else:
                j += 1
            
        return cnt
       
        