class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        newLL = result
        while list1 and list2:
            if list1.val < list2.val:
                newLL.next = list1
                list1 = list1.next
            else:
                newLL.next = list2
                list2 = list2.next
            newLL = newLL.next
        if list1:
            newLL.next = list1
        if list2:
            newLL.next = list2
        return result.next