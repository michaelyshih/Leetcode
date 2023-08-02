class minNode {
  constructor(val,min) {
    this.val = val;
    this.min = min;
  }
}
var MinStack = function() {
    this.stack = []
    this.lastNode = this.lastNode = this.stack[this.stack.length-1]
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    let prevMin
    if (!this.lastNode){
        prevMin  = val 
    }else{
        prevMin = this.lastNode.min
    }
    newMin = Math.min(prevMin,val)
    node = new minNode(val,newMin)
    this.stack.push(node)
    this.lastNode = this.stack[this.stack.length-1]
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.pop()
    this.lastNode = this.stack[this.stack.length-1]
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    this.lastNode = this.stack[this.stack.length-1]
    if (this.lastNode) return this.lastNode.val
    return 
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.lastNode.min
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */