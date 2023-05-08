/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let ans = [] 
    
    const _bts = function (i, subset, total){
        
        if (total == target){
                ans.push([...subset])
                return
        }
        
        if ( i >= candidates.length || total > target){
            return 
        }
        // keep pushing in instance of candidate at i and at the bts of that into the subset
        
        subset.push(candidates[i])
        _bts(i, subset, total + candidates[i])
        subset.pop()
        _bts(i+1, subset, total)
    }
    _bts(0,[],0)
    return ans
};