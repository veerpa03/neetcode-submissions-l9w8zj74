# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        new_head = dummy
        
        while new_head:
            curr  = new_head.next
            while curr and curr.val == val:
                curr = curr.next
            new_head.next = curr
            new_head = new_head.next
        

        return dummy.next