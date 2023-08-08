/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let [max1,max2] = [nums[0],nums[1]]
    for (let i = 2; i < nums.length;i++){
        let curr = nums[i]
        if (curr > max1){
            curr = max1
            max1 = nums[i]
        }
        if (curr > max2) max2 = curr
    }
    console.log(max1, max2)
    return (max1 - 1) * (max2 - 1) 
};