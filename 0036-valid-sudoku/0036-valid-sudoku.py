class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = {}
            col = {}
            box = {}
            row_cube = 3 * (i//3)
            col_cube = 3 * (i%3)
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in row:
                    return False
                row[board[i][j]] = 1
                if board[j][i] != '.' and board[j][i] in col:
                    return False
                col[board[j][i]] = 1
                rc = row_cube + j//3
                cc = col_cube + j%3
                if board[rc][cc] != '.' and board[rc][cc] in box:
                    return False
                box[board[rc][cc]] = 1
        return True
                
            
            