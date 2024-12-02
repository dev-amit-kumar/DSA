class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], N: int) -> Optional[ListNode]:
        fast, slow = head, head

        for i in range(N): fast = fast.next

        if fast is None: return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        delNode = slow.next
        slow.next = slow.next.next
        delNode = None

        return head