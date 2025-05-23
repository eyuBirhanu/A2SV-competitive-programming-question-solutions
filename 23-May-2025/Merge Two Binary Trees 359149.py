# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        ansVal = None  
        if root1 and root2:
            ansVal = root1.val + root2.val
        elif root1 and not root2:
            ansVal = root1.val
        elif not root1 and root2:
            ansVal = root2.val
        ans = TreeNode(ansVal)

        ans.left = self.mergeTrees(root1.left if root1 else None,
         root2.left if root2 else None)
        ans.right = self.mergeTrees(root1.right if root1 else None,
         root2.right if root2 else None)
        return ans

        