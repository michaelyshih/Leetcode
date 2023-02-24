/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let string = x.toString();
    let reverse = string.split("").reverse().join("")
  return  string === reverse;
};