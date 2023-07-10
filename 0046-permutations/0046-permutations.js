/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let ans = []
    
    if (nums.length <= 1){
        return [[...nums]]
    }
    
    nums.forEach(i =>{
        let head = nums.shift()
        // console.log(nums)
        let perms = permute(nums)
        
        // console.log(perms)
        
        for (let perm of perms){
            // console.log(perm, head)
            perm.push(head)
        }
        // console.log(perms)
        ans = ans.concat(perms)
        // console.log(ans)
        nums.push(head)
    })
    
    return ans
};