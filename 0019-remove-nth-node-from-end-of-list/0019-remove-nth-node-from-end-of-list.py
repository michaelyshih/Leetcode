# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # when n = 0, prev to next, next to next next, next= prev prev
        # dummy = ListNode(0,head)
        # slow = dummy
        # fast = head
        # while n >= 1 and fast:
        #     fast = fast.next
        #     n-=1
        # while fast:
        #     slow = slow.next
        #     fast = fast.next
        # slow.next = slow.next.next
        # return dummy.next
        
        slow = fast = head 
        
        for i in range(n):
            fast = fast.next 
        
        if not fast: return head.next
        
        while fast.next:
            slow = slow.next 
            fast = fast.next 
        slow.next = slow.next.next 
        
        return head