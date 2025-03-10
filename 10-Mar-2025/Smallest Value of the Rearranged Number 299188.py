# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            to_str = list(str(num))
            to_num = list(map(int, to_str[1:])) 
            to_num.sort(reverse=True)
            to_num.insert(0, '-')
            to_str = ''.join(list(map(str, to_num)))
            return int(to_str)
        else:
            to_str = list(str(num))
            to_num = list(map(int, to_str)) 
            to_num.sort()
            if to_num[0] == 0:
                for i in range(len(to_num)):
                    if to_num[i] > 0:
                        to_num[0], to_num[i] = to_num[i], to_num[0]
                        break
            to_str = ''.join(list(map(str, to_num)))
            return int(to_str)

            