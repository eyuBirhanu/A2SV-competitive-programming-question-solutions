# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# i
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        item = root.val
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val != item:
                return False 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True