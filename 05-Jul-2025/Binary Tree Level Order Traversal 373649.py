# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return [] 
        res = []
        q = deque()
        curr = []
        q.append(root)
        while q:
            curr = []
            for n in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(curr)
            # node = q.popleft()
            # curr.append(node.val)
            # if not q:
            #     res.append(curr)
            #     curr = []
            # if node.left: q.append(node.left)
            # if node.right: q.append(node.right)
        return res 