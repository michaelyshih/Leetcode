/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let max = 0;
    let i = 0;
    let substring = new Set();
    
    for (let j= 0; j < s.length; j++ ){
        while (substring.has(s[j])){
            substring.delete(s[i]);
                i += 1;
        }
        substring.add(s[j]);
        max = Math.max(max, substring.size)
    }
  return max
};