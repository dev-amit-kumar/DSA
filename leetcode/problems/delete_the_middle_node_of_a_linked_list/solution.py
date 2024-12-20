# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        prev = head
        slow = head
        fast = head
        while fast and fast.next and slow:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head
        