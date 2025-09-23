# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_, max_):
            if not node:
                return True
            if node.val <= min_ or node.val >= max_:
                return False
            return helper(node.left, min_, node.val) and helper(node.right, node.val, max_)
        
        return helper(root, float('-inf'), float('inf'))