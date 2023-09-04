"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        queue = [root] if root else []
        result = []
        while queue:
            node = queue.pop()
            result.insert(0,node.val)
            for child in node.children:
                queue +=child,
        return result