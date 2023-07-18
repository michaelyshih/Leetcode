# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # head of list1 and list2
        # compare c1 and c2 
        # whichever is smaller, reposition pointer, then change the next to the other pointer
        # when one .next hits None, attach the rest of the list
        # head = ans = ListNode()
        # while list1 or list2:
        #     if list1 == None:
        #         ans.next = list2
        #         break 
        #     elif list2 == None: 
        #         ans.next = list1
        #         break
        #     else:
        #         if list1.val < list2.val:
        #             ans.next = list1
        #             list1 = list1.next
        #         else:
        #             ans.next = list2
        #             list2 = list2.next
        #     ans = ans.next
        # return head.next
        
        if list1 == None: return list2
        if list2 == None: return list1
        
        if list1.val < list2.val:
            # nextlist = list1.next #save location because will lose if reassigned
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            # nextlist = list2.next
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2