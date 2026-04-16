# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast,slow = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
    
        prev = None
        curr = slow.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        l1 = head
        l2 = prev

        while l1 and l2:
            if l1.val!=l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True

        