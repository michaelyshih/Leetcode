/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  let i = 0;
  while( strs[0][i] && strs.every(word => word[i] === strs[0][i])){
    i++
  }
  return strs[0].slice(0,i)
};

console.log(longestCommonPrefix(["flower","flow","flight"]));
console.log(longestCommonPrefix(["dog","racecar","car"]));