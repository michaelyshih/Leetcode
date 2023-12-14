/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const pairs = {
      ")": "(",
      "}":"{",
      "]":"["
    }
    const stack = [];

    for (let char of s ){
      if (char in pairs){
        const top = stack[stack.length-1];
          if(stack.length > 0 && top === pairs[char]){
            stack.pop();
          } else {
            return false;
          }
      } else{
        stack.push(char);
      }
    }
  return stack.length === 0;
};