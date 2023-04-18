from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        def _inbound(r,c):
            rowInbound = 0 <= r < ROWS
            colInbound = 0 <= c < COLS
            return rowInbound and colInbound
        
        # 1. Initialize a queue with starting value(s)
        queue = deque()
        queue.append((0,0,1)) #(r,c, layer)
        
        directions = ((1,0), (0,1), (-1,0), (0,-1),
                     (1,1),(1,-1),(-1,1),(-1,-1))
        
        visited = set()
        visited.add((0,0))
        
        while queue:
            # 2. pop current node from queue
            r,c,lvl = queue.popleft()
            print(r,c)
            print(lvl)
            
            # 3. process current node 
            if r == ROWS - 1 and c == COLS - 1:
                return lvl
            
            for dir in directions:
                
                newRow = r + dir[0]
                newCol = c + dir[1]
                
                # 4. push neighbors into queue if they are valid
                print("new:", newRow, newCol)
                if _inbound(newRow, newCol) and grid[newRow][newCol] != 1 and (newRow, newCol) not in visited:
                    print("new:", newRow, newCol, "lvl:", lvl +1)
                    queue.append((newRow, newCol, lvl + 1))
                    visited.add((newRow, newCol))
                
        
        # 5. rpeat steps 2-4 until queue is empty
        return -1   