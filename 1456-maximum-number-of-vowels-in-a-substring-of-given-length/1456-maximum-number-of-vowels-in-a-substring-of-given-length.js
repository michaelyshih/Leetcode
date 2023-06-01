/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
//     window length < k
//     check how many vowels are in window 
//     return max number of vowels in set of window 
    let [l,r] = [0 , k -1]
    vowels = "AEIOUaeiou"
    vowelCount = 0 
    consCount = 0
//     s[l] + s[r] 

//     hash["aeiou"] = 1 
//     hash["none"] = 2
//     hash["aeiou"] + hash["none"] = k 
//     move left and move right add and remove from the hash + check if maxVowels > currentvowels 
    
    for (let i = 0; i <= r; i++){
            if (vowels.includes(s[i])){
                vowelCount += 1 
            }else {
                consCount += 1 
            }
        } 
    
    maxCount = vowelCount 
    
    while (r < s.length){
        r += 1
        if (vowels.includes(s[r])){
                vowelCount += 1 
        }else {
                consCount += 1 
        }
        
        if (vowels.includes(s[l])){
                vowelCount -= 1 
        }else {
                consCount -= 1 
        }
        l += 1 
        
        if (vowelCount > maxCount) maxCount = vowelCount
        
    } 
    return maxCount
    
    
    
};