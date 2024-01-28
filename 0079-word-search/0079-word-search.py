class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def _bt(r,c,i):
            if i == len(word):
                return True
            if not _inbound(r,c) or word[i] != board[r][c] or (r, c) in visited:
                return False
            
            #modify
            visited.add((r,c)) 

            #recursion
            res = ( 
                _bt(r+1, c, i+1) or
                _bt(r-1, c, i+1) or  
                _bt(r, c+1, i+1) or  
                _bt(r, c-1, i+1) )

            #backtrack
            visited.discard((r,c))
            
            return res
        
        def _inbound(r,c):
            # print(r,c)
            rInbound = r >= 0 and r < ROWS
            cInbound = c >= 0 and c < COLS
            # print(not rInbound and cInbound)
            return rInbound and cInbound

        for r in range(ROWS):
            for c in range(COLS):
                # print(r,c)
                if _bt(r,c,0):
                    # print(r,c)
                    return True

        return False