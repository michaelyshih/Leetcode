# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxNode = root.val
        
        def _dfs(root, maxNode):
            count = 0
            if maxNode <= root.val: 
                count += 1 
                maxNode = root.val
            
            if not root.left and not root.right: 
                return count 
            if root.left:
                count += _dfs(root.left,maxNode)
            if root.right:
                count += _dfs(root.right,maxNode)
            return count 
            
        return _dfs(root,maxNode)
        
        # if not root.left and not root.right: