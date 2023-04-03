/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
  if (numRows === 1) {
    return [[1]];
  }
  const prev = generate(numRows - 1);
  const last = prev[prev.length - 1];
  const next = [1];
  for (let i = 0; i < last.length - 1; i++) {
    next.push(last[i] + last[i + 1]);
  }
  next.push(1);
  prev.push(next);
  return prev;
};