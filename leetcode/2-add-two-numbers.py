# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        ans_tail = ans
        carry = 0
        while l1 or l2 or carry:
            a = (l1.val if l1 else 0)
            b = (l2.val if l2 else 0)
            carry, out = divmod(a+b + carry, 10)
            ans_tail.next = ListNode(out)
            ans_tail = ans_tail.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return ans.next
