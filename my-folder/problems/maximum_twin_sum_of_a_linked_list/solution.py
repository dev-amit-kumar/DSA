# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = float('-inf')
        stack = []
        slow, fast = head, head
        while(fast and fast.next):
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        while(stack and slow):
            val = stack.pop() + slow.val
            result = max(val, result)
            slow = slow.next
        return result