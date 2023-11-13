# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return 
        newNode = TreeNode(root.val)
        # print(newNode)
        newNode.right = self.invertTree(root.left) if root.left else None
        # print(newNode.right)
        newNode.left = self.invertTree(root.right) if root.right else None 
        # print(newNode.left)
        return newNode