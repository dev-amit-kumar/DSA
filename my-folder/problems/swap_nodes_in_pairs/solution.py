# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
		
        prev, cur = head, head.next
        prev.next = cur.next
        cur.next = prev
        head = cur
        while prev.next and prev.next.next: 
            cur = prev
            prev = prev.next
            a = prev.next

            cur.next = a
            prev.next = a.next
            a.next = prev
			
        return head