# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt = head
        curr = None
        while nxt:
            temp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = temp
        return curr
            # curr none
            # nxt 0- 1

            # 0-none
            # 1 - 2
            # 1-0-none
            # 2