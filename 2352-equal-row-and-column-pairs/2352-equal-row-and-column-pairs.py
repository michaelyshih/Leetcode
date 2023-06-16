from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = defaultdict(int)
        total = 0
        ROWS, COLS = range(len(grid)), range(len(grid[0]))
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        for row in ROWS:
            for col in COLS:
                rowMap[row].append(str(grid[row][col]))
                colMap[col].append(str(grid[row][col]))
        for col in colMap.values():
            colStr = "-".join(col)
            counter[colStr] += 1
        for row in rowMap.values(): 
            # print(row)
            rowStr = "-".join(row)
            if counter[rowStr] >= 1:
                total += counter[rowStr]
                # print(total)
        return total
        