/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let hash = {}
    for (let num of nums){
        if (hash[num] !== undefined){
            return true;
        } else{
            hash[num] = false;
        }
    }
    return false;
};