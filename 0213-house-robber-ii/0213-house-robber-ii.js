/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // same checker as house robber 1, but circular 
    // last checker to see if odd or even to see if the solution will loop 
        const robLinear = (arr) => {
        //     if (arr.length === 0) {
        //         return 0;
        //     }
        //     if (arr.length === 1) {
        //         return arr[0];
        //     }

        //     let dp = new Array(arr.length);
        //     dp[0] = arr[0];
        //     dp[1] = Math.max(arr[0], arr[1]);

        //     for (let i = 2; i < arr.length; i++) {
        //         dp[i] = Math.max(arr[i] + dp[i - 2], dp[i - 1]);
        //     }
        // return dp[arr.length - 1];
            let [rob1, rob2] = [0, 0]
            for (n of arr){
                let newRob = Math.max(rob1 + n, rob2)
                rob1 = rob2 
                rob2 = newRob
                // console.log(newRob, rob1, rob2)
            }
            return rob2
        }
        // Case 1: Exclude the last house
    const result1 = robLinear(nums.slice(0, nums.length - 1));

    // Case 2: Exclude the first house
    const result2 = robLinear(nums.slice(1));

    return Math.max(nums[0], result1, result2)
}
