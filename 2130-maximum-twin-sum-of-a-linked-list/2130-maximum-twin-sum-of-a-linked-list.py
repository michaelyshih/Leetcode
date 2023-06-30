# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head 
        prev  = None 
        while fast and fast.next: 
            fast = fast.next.next 
            temp = slow.next 
            slow.next = prev 
            prev = slow 
            slow = temp
            
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next 
            slow = slow.next
            
        return res
            
#         vals = []
#         pair = defaultdict(int)
        
#         while head:
#             vals.append(head.val)
#             head = head.next
#         n = len(vals)
        
#         for i, val in enumerate(vals):
#             if pair[n-i-1]:
#                 pair[n-i-1] += val
#             else:
#                 pair[i] += val
        
#         return max(pair.values())
