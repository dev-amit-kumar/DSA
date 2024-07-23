# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        carry = 0
        while (l1 or l2) or carry:
            newSum = 0
            if (l1):
                newSum += l1.val
                l1 = l1.next
            if (l2):
                newSum += l2.val
                l2 = l2.next
            newSum += carry
            carry = newSum // 10
            node = ListNode(newSum % 10)
            result.next = node
            result = result.next
        return dummy.next
        