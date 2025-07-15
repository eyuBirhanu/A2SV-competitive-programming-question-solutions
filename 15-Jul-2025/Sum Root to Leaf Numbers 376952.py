# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        char = [] 
        res = 0 

        def dfs(node):
            if not node:
                return 

            char.append(node.val)

            if not node.left and not node.right:
                chars = ''.join(list(map(str, char)))
                nonlocal res
                res += int(chars)
            
            dfs(node.left)
            dfs(node.right)
            char.pop()
        
        dfs(root)
        return res