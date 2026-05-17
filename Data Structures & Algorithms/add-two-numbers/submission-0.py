# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        dummy=ListNode(0)
        curr= dummy
        while l1 or l2 or extra:
            total = 0
            if l1:
                total += l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            if extra==1:
                total += 1
            if total>=10:
                extra =1
                total -=10
            else:
                extra = 0
            curr.next = ListNode(total,None)
            curr=curr.next
        return dummy.next