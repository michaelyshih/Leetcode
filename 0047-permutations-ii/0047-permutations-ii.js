/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    let res,  perm, count 
    res = [] 
    perm = []
    count= {}
    
    for ( let n of nums){
        if (count[n] != undefined){
            count[n] += 1
        }else{
            count[n] = 1
        }
    }
    
    var _bts = ()=>{
    
    if (nums.length == perm.length){
        res.push([...perm])
        // console.log(res)
        return
    }
        
    
    for (let key of Object.keys(count)){
        // console.log(key)
        if (count[key] > 0){
            perm.push(key)
            count[key] -= 1
            _bts()
            count[key] += 1
            perm.pop()
        }
        
    }
        
    }
    _bts()
    return res
};