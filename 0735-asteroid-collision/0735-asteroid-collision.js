/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
    stack = []
    for (let a of asteroids){
       while (stack.length && a < 0 && stack[stack.length-1] > 0){
           let diff = a + stack[stack.length-1]
           if (diff < 0){
               stack.pop()
               console.log(stack)
           }else if(diff > 0){
               a = 0
           }else{
               a = 0
               stack.pop()
           }
        }
        if(a) stack.push(a)
    }
    return stack
};