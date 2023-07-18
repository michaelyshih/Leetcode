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
  let currentInterval = sortedIntervals[0];
  merged.push(currentInterval);

  for (const nextInterval of sortedIntervals) {
    const [_, currentIntervalEnd] = currentInterval;
    const [nextIntervalStart, nextIntervalEnd] = nextInterval;

    if (currentIntervalEnd >= nextIntervalStart) {
      // If current and next intervals overlap, then merge them
      currentInterval[1] = Math.max(currentIntervalEnd, nextIntervalEnd);
    } else {
      currentInterval = nextInterval;
      merged.push(currentInterval);
    }
  }

  return merged;
};