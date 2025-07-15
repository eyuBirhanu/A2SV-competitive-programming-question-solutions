# Problem: Path Sum II - https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        sub = []

        def dfs(node):
            if not node:
                return
            
            sub.append(node.val)

            if not node.left and not node.right:
                if sum(sub) == targetSum:
                    res.append(sub.copy())

            dfs(node.left)
            dfs(node.right)
            val = sub.pop()

        dfs(root)

        return res 