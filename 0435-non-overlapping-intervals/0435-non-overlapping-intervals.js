/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    intervals.sort((a,b) =>{
        if (a[0] < b[0]){
            return -1
        }else if (a[0] > b[0]){
            return 1
        }else{
            if (a[1] <= b[1]){
                return -1
            }else{
                return 1
            }
        }
    })
    let count = 0 
    let prevEnd = intervals[0][1]
    for (let interval of intervals.slice(1)){
        // console.log(interval)
        let [start, end] = interval 
        if (start >= prevEnd){
            prevEnd = end 
        }else{
            count += 1
            prevEnd = Math.min(end, prevEnd)
        }
    }
    return  count
};