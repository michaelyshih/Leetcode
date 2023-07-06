# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# check to see if either chilren returns values 
# if both children returns values return self 
# if one children returns values return self only if self is a value 
# else return the chilren's value 


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        
        if cur == p or cur == q: 
            return cur
        
        left, right = None, None
        
        if root.left:
            left = self.lowestCommonAncestor(root.left,p,q)
        if root.right:
            right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right: 
            return cur
        elif left: 
            return left 
        else: 
            return right
        