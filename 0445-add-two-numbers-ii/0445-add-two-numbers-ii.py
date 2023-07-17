# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1 = []
        stack2 = [] 
        while l1: 
            stack1.append(l1.val)
            l1 = l1.next 
        while l2: 
            stack2.append(l2.val)
            l2 = l2.next 
        
        carry = 0 
        result = None
        while len(stack1) > 0 or len(stack2) > 0:
            a, b = 0, 0 
            if len(stack1) > 0:
                a = stack1.pop()
            if len(stack2) > 0: 
                b = stack2.pop()
            total = a + b + carry
            
            temp = ListNode(total % 10)
            carry = total // 10
            
            if not result: 
                result = temp 
            else:
                temp.next = result 
                result = temp 
        if not carry == 0: 
            temp = ListNode(carry)
            temp.next = result 
            result = temp 
        return result