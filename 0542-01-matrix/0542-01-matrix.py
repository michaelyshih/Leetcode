class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        
        def _inbound(r,c):
            rowInbound = 0 <= r < ROWS
            colInbound = 0 <= c < COLS
            return rowInbound and colInbound
        
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = -1 # placeholder until processed
        
        while queue:
            row, col = queue.popleft()
            for dir in directions:
                newRow, newCol = row + dir[0], col + dir[1]
                if not _inbound(newRow, newCol) or mat[newRow][newCol] != -1: continue
                    
                mat[newRow][newCol] = mat[row][col]+1
                queue.append((newRow,newCol))
                
        return mat