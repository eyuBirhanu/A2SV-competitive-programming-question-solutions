# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 3
        def simulate(node, sum_):
            if not node:
                return False
            if not node.left and not node.right:
                if sum_+ node.val == targetSum:
                    return True
            sum_ += node.val
            return simulate(node.left, sum_) or simulate(node.right, sum_)
        
        if not root:
            return False
        return simulate(root, 0) or False
