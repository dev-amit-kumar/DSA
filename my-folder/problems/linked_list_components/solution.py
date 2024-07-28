# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        component = 0
        running = False
        while(head):
            if (head.val in nums):
                if (not running):
                    running = True
                    component += 1
                nums.remove(head.val)
            else:
                running = False
            head = head.next
        return component

