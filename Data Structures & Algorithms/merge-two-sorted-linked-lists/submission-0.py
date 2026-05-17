# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0,None)
        r = ListNode(0,res)
        while list1 or list2:
            if list1 == None:
                res.next = list2
                list2 = list2.next
            elif list2 == None:
                res.next = list1
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    res.next = list2
                    list2 = list2.next
                else:
                    res.next = list1
                    list1 = list1.next
            res = res.next
        return r.next.next