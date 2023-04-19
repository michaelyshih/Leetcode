class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) -1
        results = []
        
        def _backtrack(currNode, path):
            if currNode == target:
                results.append(list(path)) # have to append a copy of path.
                return
            
            for neighbor in graph[currNode]:
                path.append(neighbor)
                _backtrack(neighbor, path)
                path.pop()
        
        path = [0]
        _backtrack(0,path)
        
        return results