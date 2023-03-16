/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let words = s.trim().split(" ");
    let last = words[words.length-1]
    return last.length
};