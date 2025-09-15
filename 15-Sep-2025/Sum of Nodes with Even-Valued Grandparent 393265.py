# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grandParent):
            if not node:
                return 0

            sum_ = node.val if grandParent and grandParent.val % 2 == 0 else 0

            sum_ += dfs(node.left, node, parent)
            sum_ += dfs(node.right, node, parent)

            return sum_ 

        return dfs(root, None, None)