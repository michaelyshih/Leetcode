/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if (!head.next){
        return null
    }
    
    turtle = head
    prev = new ListNode()
    prev.next = turtle
    hare = head 
    
    while (turtle && hare && turtle.next && hare.next){
        turtle = turtle.next
        hare = hare.next.next
        prev = prev.next
    }
    prev.next = turtle.next

    

    return head
};