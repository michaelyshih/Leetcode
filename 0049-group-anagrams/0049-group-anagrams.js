/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
 let dictionary = {}
    for (s of strs){
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
	return [...str].sort().join('');
}