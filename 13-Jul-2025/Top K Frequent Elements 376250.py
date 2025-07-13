# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        # klkl
        for num in nums:
            if num not in dict_:
                dict_[num] = nums.count(num)
        sorted_dict = dict(sorted(dict_.items(), 
                                  key=lambda item: item[1],
                                  reverse = True)) 
        result = []
        for items, values in sorted_dict.items():
            if len(result) < k:
                result.append(items)
        return result