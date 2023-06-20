/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    let res = [] 
    let pacific = new Set()
    let atlantic = new Set()
    
    let ROWS = heights.length
    let COLS = heights[0].length
    
    const _inBound = (r,c) => {
        let rowBound = (r >= 0) && (r < ROWS)
        let colBound = (c >= 0) && (c < COLS)
        return rowBound && colBound
    }
    
    const _dfs = (r,c,visited,prevHeight) => {
        if (!_inBound(r,c) || visited.has(`${r + "," + c}`) || heights[r][c] < prevHeight){
            return 
        }
        visited.add(`${r + "," + c}`)
        
        const DIRECTIONS = [ [0,1] , [1,0] , [-1,0] , [0,-1] ]
        
        for (dir of DIRECTIONS){
            newR = r + dir[0]
            newC = c + dir[1]
            // console.log(visited)
            _dfs(newR, newC, visited, heights[r][c])
        }
        return
    }
    
    for (let c = 0; c < COLS; c++){
        _dfs(0 , c, pacific, heights[0][c])
        _dfs(ROWS - 1, c, atlantic, heights[ROWS-1][c])
    }
    for (let r = 0; r < ROWS ; r++){
        _dfs(r, 0, pacific, heights[r][0])
        _dfs(r, COLS-1, atlantic, heights[r][COLS-1])
    }
    for (pair of pacific){
        if (atlantic.has(pair)){
            let [r,c] = pair.split(",")
            res.push([r,c])
        }
    }
    return res
};