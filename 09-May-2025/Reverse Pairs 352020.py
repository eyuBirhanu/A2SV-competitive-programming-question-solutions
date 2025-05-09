# Problem: Reverse Pairs - https://leetcode.com/problems/reverse-pairs/description/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self._merge_count(nums, 0, len(nums)-1)
    def _merge_count(self, a: List[int], lo: int, hi: int) -> int:
        if lo >= hi:
            return 0
        
        mid = (lo + hi) // 2
        cnt = self._merge_count(a, lo, mid) + self._merge_count(a, mid + 1, hi)

        j = mid + 1
        for i in range(lo, mid + 1):
            while j <= hi and a[i] > 2 * a[j]:
                j += 1
            cnt += j - (mid + 1)
        temp = []
        i, j = lo, mid+1
        while i <= mid and j <= hi:
            if a[i] <= a[j]:
                temp.append(a[i])
                i += 1
            else:
                temp.append(a[j])
                j += 1
        temp.extend(a[i:mid+1])
        temp.extend(a[j:hi+1])
        a[lo:hi+1]=temp
        return cnt