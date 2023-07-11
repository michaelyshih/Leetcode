# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = defaultdict(TreeNode)
        
#         create a parent to child relationship map
        def _preOrder(root,par):
            if not root: return 
            
            parent[root] = par
            _preOrder(root.left,root)
            _preOrder(root.right,root)
        
        _preOrder(root,None)
        
        q = deque()

        q.append(target)
        visited = set()
        
        while len(q) > 0 and k > 0: 
            k -= 1 
            
            for i in range(len(q)): 
                curr = q.popleft()
                visited.add(curr)
                # if curr: print(curr.val, parent[curr].val)
                if curr.left: print(curr.left.val, not curr.left in visited)
                if curr.right: print(curr.right.val, not curr.right in visited)


                if curr.left and not curr.left in visited: q.append(curr.left)
                if curr.right and not curr.right in visited: q.append(curr.right)
                if parent[curr] and not parent[curr] in visited: q.append(parent[curr])
                    
        q = list(map(lambda x: x.val, list(q)))
        
        return q
    
        