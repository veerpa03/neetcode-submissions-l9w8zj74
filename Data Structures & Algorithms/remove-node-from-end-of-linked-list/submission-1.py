# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        lenght = 0
        while curr :
            curr = curr.next 
            lenght+=1
        curr = head
        if lenght == n:
            head = head.next
            return head
        for i in range(lenght):
            if i == (lenght-n)-1:
                curr.next =curr.next.next
                return head
            curr = curr.next

