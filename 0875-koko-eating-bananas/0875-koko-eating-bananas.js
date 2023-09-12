/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */

// maximum k for each pile 
// find minimum k where she would finish all index 
// sort the array 

// given a possible k, go through array with possible rate
// if possible rate is higher than k then break out say too small 
// having a rate for the for where it will not exceed h 

// helper to check the number in the array and return how many hours it will require

var minEatingSpeed = function(piles, h) {
    let [l,r] = [1,Math.max(...piles)]
    let res = r
    while (l <= r){
        mid = Math.floor((l+r)/2)
        totalHours = 0 
        for (p of piles){
            totalHours += Math.ceil(p/mid)
        }
        if (totalHours <= h){
            res = mid
            r = mid - 1
        }else{
            l = mid + 1
        }
    }
    return res
}