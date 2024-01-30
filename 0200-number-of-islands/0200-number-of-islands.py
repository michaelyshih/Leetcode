class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        visited = set()


        def _dfs(row, col):
            if not _inbound(row,col):
                return False

            pos = f'{row},{col}'
            if pos in visited:
                return False
            
            if grid[row][col] == '0':
                return False

            visited.add(pos)

            #tupel, array that cannot be mutated 
            directions = ((1,0), (0,1),(-1,0),(0,-1))

            for (x,y) in directions: 
                newRow = row + x
                newCol = col + y
                _dfs(newRow , newCol)

            return True

        def _inbound(row,col):
            rInbound = 0 <= row and row < len(grid)
            cInbound = 0 <= col and col < len(grid[0])
            return rInbound and cInbound



        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if _dfs(row,col):
                    count += 1
        return count 