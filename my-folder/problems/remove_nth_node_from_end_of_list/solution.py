# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], N: int) -> Optional[ListNode]:
        fastp = head
        slowp = head

        # Move the fastp pointer N nodes ahead
        for i in range(N):
            fastp = fastp.next

        # If fastp becomes None, the Nth node from the end is the head
        if fastp is None:
            return head.next

        # Move both pointers until fastp reaches the end
        while fastp.next is not None:
            fastp = fastp.next
            slowp = slowp.next

        # Delete the Nth node from the end
        delNode = slowp.next
        slowp.next = slowp.next.next
        delNode = None
        return head