/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
 let dictionary = {}
    for (s of strs){
//         for every word in arr, reorder the char in words
        key = reorderStr(s);
        if (dictionary[key] === undefined){
            dictionary[key] = [s]
        } else {
            dictionary[key] = dictionary[key].concat(s)
        }
    }
    return Object.values(dictionary)
};

function reorderStr(str) {
	return str.split('').sort().join('');
}