# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 1, len(skill)-2
        chemisry = 0
        target = skill[0] + skill[-1]
        first = (skill[0] * skill[-1])
        chemisry += first
        while i < j:
            if skill[i] + skill[j] == target:

                chemisry +=  (skill[i] * skill[j])
                i ,j = i+1, j-1
            else:
                return -1
        return chemisry

        