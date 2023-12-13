/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let [res, temp] =[ nums[0] , 0 ]
    for (let num of nums){
        if (temp  < 0 ){
            temp = num
        }
        else{
            temp += num 
        }
        res = Math.max(res, temp)
    }
    return res
};

//  for loop through, when the sum is neg, 
//          move left pointer basically to where positive 
//  new negative, ignore

// temp sum and final sum 
// what can you do to the temp to get to bigger sum 

