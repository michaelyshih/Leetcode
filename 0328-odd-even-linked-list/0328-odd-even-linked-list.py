# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#         run through list if count is even connect to next next  
#         if count is odd then create a dummy and attach to the end of even linked list when next is undefined 
#         when at end of odd, connect all the evens 
#         when at end of even, put into the end and prev is the last connection

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head 
        
        oddP = current = head 
        eveP = evenhead = head.next 
        current = current.next.next 
        # print (current)
        i = 1
        
        def _end(eveP, evenhead, oddP, current):
            oddP.next = evenhead
            eveP.next = None
            current = None
            return 
        
        while current:
            oddP.next = current 
            oddP = oddP.next
            if current.next and current.next.next:
                eveP.next = current.next
                eveP = eveP.next
                current = current.next.next
            elif current.next:
                eveP.next = current.next
                eveP = eveP.next
                _end(eveP, evenhead, oddP, current)
                break
            else:
                _end(eveP, evenhead, oddP, current)
                break
        
#         while current: 
#             if i > 2 and i % 2 != 0:
#                 oddP.next = current 
#                 print(current)
#                 oddP = oddP.next
                
#             elif i > 2 and i % 2 == 0:
#                 eveP.next = current
#                 eveP = eveP.next
#             current = current.next 
#             i += 1 

#         oddP.next = evenhead
#         eveP.next = None
        
        return head
                
                
            