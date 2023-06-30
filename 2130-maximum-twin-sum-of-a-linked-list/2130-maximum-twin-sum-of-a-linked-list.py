# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        pair = defaultdict(int)
        
        while head:
            vals.append(head.val)
            head = head.next
        n = len(vals)
        
        for i, val in enumerate(vals):
            if pair[n-i-1]:
                pair[n-i-1] += val
            else:
                pair[i] += val
        
        return max(pair.values())