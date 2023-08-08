/**
 * @param {string[]} queries
 * @param {string[]} dictionary
 * @return {string[]}
 */
var twoEditWords = function(queries, dictionary) {
    let res = [] 
    for(let query of queries){
        for (let word of dictionary){
            let count =  0 
            let i =  0 
            while (i < query.length){
                if (query[i] !== word[i]) count++
                i++
            }
            if (count <= 2){
                res.push(query)
                count = 0 
                break
            }   
        }
    } 
    return res
};