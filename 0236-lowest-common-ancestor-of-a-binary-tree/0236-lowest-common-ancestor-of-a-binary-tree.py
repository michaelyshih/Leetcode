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
        # def _dfs(root,p,q,res,anc):
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
            
#             if len(res) < 2 and (root == p or root == q): 
#                 res.append(root)
#                 # if len(res) >= 2:
#                 return res
            
#             if not root.left and not root.right: return []
            
#             right, left = None, None
            
#             if len(res) < 2 and root.left:
#                 left = _dfs(root.left,p,q,res,anc)
#                 # print(root.val, len(res), res[0].val, left[0].val)
#                 if left and left[0] == res[0] and len(res) == 1:
#                     print("hit")
#                     res[0] = root
#                 print(root.val, res[0].val, len(res),left)
#                 if len(res) >= 2:
#                     return res
                
#             if len(res) < 2 and root.right:
#                 right =  _dfs(root.right,p,q,res,anc)
#                 print(res,left)
#                 if len(res) == 2 and left and :
#                     res = [root,res[1]]
#                 print("after root:", res)
#                 if len(res) >= 2:
#                     return res
            
#             # if right: print(right)
                
#             return res
            
#         res = _dfs(root,p,q,[],root)
#         # print(res)
#         return res[0]
        
            
        