/**
 * @param {number} num
 * @return {boolean}
 */
var sumOfNumberAndReverse = function(num) {
    if (num==0) return true
    let str = num.toString()
    for (let i = 0; i < num; i++){
        let rev = parseInt(i.toString().split("").reverse().join(""),10)
        if (i + rev == num){
            return true
        }
    }
    return false
};