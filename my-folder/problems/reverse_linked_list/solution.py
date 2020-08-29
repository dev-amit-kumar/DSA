# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head 
        while(current is not None): 
            temp = current.next
            current.next = prev 
            prev = current 
            current = temp
        head = prev
        return head
