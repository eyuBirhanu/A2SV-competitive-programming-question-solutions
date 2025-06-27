# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(nums[len(nums)//2])
        def create(l, r):
            if l > r:
                return 
            mid = (l+r)//2
            left = create(l, mid-1)
            right = create(mid+1, r)
            return TreeNode(nums[mid], left, right)
        return create(0, len(nums)-1)
