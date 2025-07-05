# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 
        
        res = []
        q = deque()
        curr_arr = []
        curr_level = 0
        
        q.append((root, 0))
        
        while q:
            node, level = q.popleft()
            
            if level == curr_level:
                curr_arr.append(node.val)
            else:
                res.append(curr_arr)
                curr_arr = [node.val]
                curr_level = level 
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        res.append(curr_arr) 
        return res
