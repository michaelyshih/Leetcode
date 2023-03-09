/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length === 0 || nums.length === 1){
        return nums.length;
    }
    var left = 0 
    for (var right = 0; right < nums.length; right ++){
        if (nums[right] !== nums [right+1]){
            nums[left++] = nums[right]
        }
    }
    return left
};