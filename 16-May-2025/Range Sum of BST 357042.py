# Problem: Range Sum of BST - https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_ = 0
        def traverse(node):
            if node:
                if node.val in range(low, high+1):
                    nonlocal sum_
                    sum_ += node.val
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return sum_
