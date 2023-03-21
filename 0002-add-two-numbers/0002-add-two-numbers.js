/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
        let carry = 0;
    let result = new ListNode(-1);
    let dummy = result;
        
    while (l1 || l2 || carry){
        let val1 = l1 ? l1.val : 0;
        let val2 = l2 ? l2.val : 0;
        let sum = (val1 + val2 + carry);
        result.next = new ListNode(sum % 10);
        result = result.next 
        carry = Math.floor(sum /10)
        l1 = l1 ? l1.next: null;
        l2 = l2 ? l2.next: null;
        console.log(result)
        console.log(dummy)
    }
    return dummy.next
};