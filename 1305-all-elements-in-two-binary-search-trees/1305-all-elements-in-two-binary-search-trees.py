# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sortedcontainers import SortedList
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        q = deque([root1,root2])
        l = SortedList()
        
        while len(q) > 0: 
            curr = q.popleft()
            if not curr: continue
            l.add(curr.val)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        
        return l
        