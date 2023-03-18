/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let result = []
    let carry = 0;
    let i = a.length -1;
    let j = b.length - 1;
    while (i >= 0 || j >= 0 || carry !== 0){
      if(i >= 0){
        carry += parseInt(a[i]);
        i--;
      }
      if (j >= 0){
        carry += parseInt(b[j]);
        j--;
      }
      result.push((carry % 2).toString());
      carry = Math.floor(carry / 2);
    } 
  return result.reverse().join("");
};