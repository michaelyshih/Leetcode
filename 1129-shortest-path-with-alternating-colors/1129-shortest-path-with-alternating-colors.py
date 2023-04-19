from collections import deque, defaultdict
class Solution:
    
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        red = defaultdict(list)
        blue = defaultdict(list)
        
        for src, dst in redEdges: 
            red[src].append(dst)
        for src, dst in blueEdges:
            blue[src].append(dst)
        
        #initialize queue with starting node
        answer = [-1 for _ in range(n)]
        queue = deque([(0,0,None)]) # (node, length, prev_edge_color)
        visited = set([(0,None)]) # (node, prev_edge_color)
        
        while queue: 
            #shift current node out from queue
            node, length, edgeColor = queue.popleft()
            
            #process node
            if answer[node] == -1:
                answer[node] = length
            
            #push all valid neightbors into queue 
            if edgeColor != "RED":
                for neighbor in red[node]:
                    if (neighbor, "RED") not in visited: 
                        visited.add((neighbor, "RED"))
                        queue.append((neighbor, length+1, "RED"))
                    
            if edgeColor != "BLUE":
                for neighbor in blue[node]:
                    if (neighbor, "BLUE") not in visited: 
                        visited.add((neighbor, "BLUE"))
                        queue.append((neighbor, length+1, "BLUE"))
        
        return answer