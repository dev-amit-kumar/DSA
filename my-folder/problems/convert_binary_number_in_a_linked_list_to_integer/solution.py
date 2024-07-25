# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def getString(head):
            if not head:
                return ''
            elif not head.next:
                return str(head.val)
            else:
                return str(head.val) + getString(head.next)
        return int(getString(head), 2)