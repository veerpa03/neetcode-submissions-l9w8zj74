# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if slow==None:
            return False
        while fast.next!=None:
            slow = slow.next 
            fast = fast.next.next
            if fast == None:
                break
            if fast == slow:
                return True
        return False