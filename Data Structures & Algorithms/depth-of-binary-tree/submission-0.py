# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0

        def explore(node, depth):
            nonlocal count 

            if not node:
                return 0
            
            count = max(count, depth)

            explore(node.left, depth+1)
            explore(node.right, depth+1)

            return count
        
            

        explore(root, 1)
        return count
