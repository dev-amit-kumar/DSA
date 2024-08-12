# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_map = []
        while headA or headB:
            if headA == headB:
                return headA
            if headA:
                if headA in hash_map:
                    return headA
                else:
                    hash_map.append(headA)
                headA = headA.next
            if headB:
                if headB in hash_map:
                    return headB
                else:
                    hash_map.append(headB)
                headB = headB.next
        return None
