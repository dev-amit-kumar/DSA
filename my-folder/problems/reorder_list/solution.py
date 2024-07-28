class Solution:
    def reverseLL(self, head):
        if head is None or head.next is None:
            return head
        last_node = self.reverseLL(head.next)
        head.next.next = head
        head.next = None
        return last_node

    def middleLL(self, head):
        fast = head
        slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = self.middleLL(head)
        reverseHead = self.reverseLL(slow.next)
        slow.next = None
        curr = head
        while(head and reverseHead):
            nextHead = head.next
            nextReverseHead = reverseHead.next
            head.next = reverseHead
            reverseHead.next = nextHead

            head = nextHead
            reverseHead = nextReverseHead
        