# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(s) > 12:
            return res

        def backTrack(i, dots, currIP):
            if dots == 4 and i == len(s):
                res.append(currIP[:-1])
                return
            if dots > 4:
                return
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) <= 255 and (i == j or s[i] != '0'):
                    backTrack(j+1, dots+1, currIP + s[i:j+1] + '.')

        backTrack(0, 0, '')
        return res