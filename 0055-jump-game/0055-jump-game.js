/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let end = nums.length -1 
    for (let i = end; i >= 0;i--){
        if (i + nums[i] >= end){
            end = i
        }
    }
    return end == 0
};