/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    let ans = [] 
    let subset = [] 
    const  _bt = function(i){
        if (i >= nums.length){
            ans.push([...subset])
            return
        }
        subset.push(nums[i])
        _bt(i+1)
        subset.pop()
        _bt(i+1)
    }
    _bt(0)
    return ans 
};