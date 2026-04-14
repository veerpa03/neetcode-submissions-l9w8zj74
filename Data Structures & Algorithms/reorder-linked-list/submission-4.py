# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        dummy = ListNode()

        list1 = head
        list2 = slow.next
        slow.next = None

        prev = None
        curr = list2
        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        list2 = prev

        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            curr.next = list1
            list1 = list1.next
            curr= curr.next
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
