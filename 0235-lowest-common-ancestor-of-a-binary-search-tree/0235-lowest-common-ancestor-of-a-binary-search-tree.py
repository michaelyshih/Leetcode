# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         under the assumption that they're unique and sorted 
        cur = root 
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# find the two nodes then find where they merge 
# path from root to node 
# unqie or not and may not be sorted 
# path of travel 
# 

# 6,2,
# 6,2,4
# passed = [0,2,3,4]

# 6,8,9
