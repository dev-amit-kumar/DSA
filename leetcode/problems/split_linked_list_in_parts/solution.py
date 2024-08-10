# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        dummy = head
        while(dummy):
            length += 1
            dummy = dummy.next
        count = length // k
        reminder = length % k
        ans = []
        for i in range(0, k):
            if not head:
                ans.append(None)
            else:
                ans.append(head)
                rem = (count) + (1 if reminder > 0 else 0)
                reminder -= 1
                for j in range(0, rem - 1):
                    head = head.next
                next_node = head.next
                head.next = None
                head = next_node
        return ans