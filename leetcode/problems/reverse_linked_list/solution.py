# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head or not head.next): return head
        newLL = ListNode()
        start = True
        while(head):
            temp = ListNode(head.val)
            if start:
                start = False
            else:
                temp.next = newLL
            newLL = temp
            head = head.next
        return newLL
