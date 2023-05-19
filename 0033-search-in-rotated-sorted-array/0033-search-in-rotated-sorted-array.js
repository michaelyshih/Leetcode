/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let [l, r] = [0, nums.length - 1] 
        while (l <= r){
            mid = Math.floor((l + r)/ 2)
            if (target === nums[mid]){
                return mid 
            }
            
            if (nums[l] <= nums[mid]){
                if (target > nums[mid] || target < nums[l]){
                    l = mid + 1
                }else{
                    r = mid - 1
                }
                
            }
            else{
                if (target < nums[mid] || target > nums[r]){
                    r = mid - 1 
                }else {
                    l = mid + 1
                }
            }
        } 
    return -1
    
};