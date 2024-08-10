# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        dummy = head
        while(dummy):
            if dummy.val == val:
                if prev is None:
                    head = head.next
                    dummy = head
                elif dummy.next is None:
                    prev.next = None
                    break
                else:
                    dummy = dummy.next
                    prev.next = dummy
            else:
                prev = dummy
                dummy = dummy.next
        return head