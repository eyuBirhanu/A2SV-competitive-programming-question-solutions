# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # sjj
        res = [[1]]
        cnt = 1
        while cnt < numRows:
            arr = deepcopy(res[-1])
            arr = [0] + arr + [0]
            subRes = []
            for i in range(len(arr)-1):
                sum_ = arr[i]+arr[i+1]
                subRes.append(sum_)
            res.append(subRes)
            cnt += 1
        return res

        