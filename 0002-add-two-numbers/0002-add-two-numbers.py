# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2:
            digit = carry 
            carry = carry
            if l1:
                digit += l1.val
                carry += l1.val
            if l2:
                digit += l2.val
                carry += l2.val
            
            digit = digit % 10
            carry = carry // 10
            print(digit, carry)
            curr.val = digit
            if l1 and l1.next:
                curr.next = ListNode()
            if l2 and l2.next:
                curr.next = ListNode()
            if carry:
                curr.next = ListNode(carry)
            
            curr = curr.next 
            l1 = l1.next if l1 else None  
            l2 = l2.next if l2 else None
            
        return dummy