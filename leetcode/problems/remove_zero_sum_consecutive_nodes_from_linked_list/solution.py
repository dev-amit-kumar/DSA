# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        hash_table = {}
        prefix_sum = 0
        
        while current:
            prefix_sum += current.val
            hash_table[prefix_sum] = current
            current = current.next
        
        prefix_sum = 0
        current = front

        while current:
            prefix_sum += current.val
            current.next = hash_table[prefix_sum].next
            current = current.next
            
        return front.next