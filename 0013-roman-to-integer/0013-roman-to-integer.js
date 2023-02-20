/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let keys = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}
    let output = 0;
    for (var i = s.length - 1; i >= 0; i--){
        if(keys[s[i+1]] > keys[s[i]]){
            output = output - keys[s[i]];
        }else{
            output = output + keys[s[i]];
        }
    }
  // return s[4] + s[3];
  return output;
    
};
