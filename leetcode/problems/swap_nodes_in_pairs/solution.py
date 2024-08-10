# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        temp = head.next
        # Swap the two nodes
        head.next = temp.next
        temp.next = head
        
        # recusrive call to swap the rest of LL
        head.next = self.swapPairs(head.next)

        return temp