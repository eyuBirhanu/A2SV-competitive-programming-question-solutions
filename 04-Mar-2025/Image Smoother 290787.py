# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        res_arr = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sum_ = 0
                count = 0
                for r in range(i-1, i + 2):
                    for c in range(j-1, j+2):
                        if r < 0 or r == rows or c < 0 or c == cols:
                            continue
                        sum_ += img[r][c]
                        count += 1
                res_arr[i][j] = sum_ // count
        return res_arr