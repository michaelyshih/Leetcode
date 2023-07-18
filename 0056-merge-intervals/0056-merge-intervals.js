/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    
  // Sort input intervals by their lower-bound
  const sortedIntervals = intervals.sort((a, b) => a[0] - b[0]);
  // Resulting array of merged intervals
  // It will serve as a stack when solving problem
  const merged = [];
  let curr = sortedIntervals[0];
  merged.push(curr);

  for (const nextInt of sortedIntervals) {
    const [_, currEnd] = curr;
    const [nxtSt, nxtEnd] = nextInt ;

    if (currEnd >= nxtSt) {
      // If current and next intervals overlap, then merge them
      curr[1] = Math.max(currEnd, nxtEnd);
    } else {
      curr = nextInt;
      merged.push(curr);
    }
  }

  return merged;
};