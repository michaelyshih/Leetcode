/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    results = []
//     sort reads negatives as string and sort them by integer
    nums.sort((a,b)=> a - b)
    
    for (let [i,ele] of nums.entries()){
        if (i > 0 && nums[i-1] == ele){
            continue 
        }
        let [l,r] = [i + 1, nums.length -1]
        
        while (l < r){
            let total = ele + nums[l] + nums[r] 
            if (total > 0){
                r -= 1 
            }else if(total < 0){
                l += 1
            }else{
                results.push( [ele, nums[l], nums[r]])
                l += 1
                while (nums[l] == nums[l-1] && l < r){
                    l += 1
                }
            }
        }
    }
    return results 
};