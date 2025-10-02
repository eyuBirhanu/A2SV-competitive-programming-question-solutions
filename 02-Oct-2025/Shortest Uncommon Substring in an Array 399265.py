# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        sub_str = []
        
        for w in arr:
            sub = set()
            for i in range(len(w)):
                for j in range(i, len(w)):
                    sub.add(w[i:j+1])
            sub_str.append(sub)

        res = []

        for i in range(len(sub_str)):
            sub = []
            for w in sub_str[i]:
                for j in range(len(sub_str)):
                    if j != i and w in sub_str[j]:
                        break
                else:
                    sub.append(w)
            res.append(sub)  

        final = []
        
        for i in range(len(res)):
            word = sorted(res[i], key=lambda x: (len(x), x))
            if len(word) > 0:
                final.append(word[0])
            else:
                final.append("")
        return final

                