from collections import deque  
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        #fresh oranges counter
        fresh = 0
        minute = 0
                
        def _inbound(r,c):
            rowInbound = 0 <= r < ROWS
            colInbound = 0 <= c < COLS
            return rowInbound and colInbound
        
        #initialize with all bad oranges 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2: 
                    queue.append((r,c,0))
                    
        if not fresh :
            return 0
        
        directions = ((1,0), (0,1), (-1,0), (0,-1))
        
        while queue:
            r, c, minute = queue.popleft()
            
            #added neighbor oranges to queue, also need to convert to rotten, decrement fresh
            for dir in directions:
                newRow = r + dir[0]
                newCol = c + dir[1]
                
                if _inbound(newRow, newCol) and grid[newRow][newCol] == 1:
                    queue.append((newRow, newCol, minute + 1))
                    grid[newRow][newCol] = 2 
                    fresh -= 1
            
        #after all the queue is popped out    
        # if fresh != 0: 
        #     return -1
        # else: 
        #     return minute 
        return minute if fresh == 0 else -1
        #keep track of level compared to length of queue 