class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def atHead(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = NewNode

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # def deleteNode(self, RemoveKey):
    #     temp = self.head
    #     if(temp):
    #         while(temp):
    #             if temp.data == RemoveKey:
    #                 break
    #             prev = temp
    #             temp = temp.next
    #     else:
    #         return

    #     prev.next = temp.next
    #     temp = None

    # def RemoveNode(self, Removekey):
    #     temp = self.head
    #     if (temp is not None):
    #         if (temp.data == Removekey):
    #             self.head = temp.next
    #             temp = None
    #             return
    #     while (temp is not None):
    #         if temp.data == Removekey:
    #             break
    #         prev = temp
    #         temp = temp.next
    #     if (temp == None):
    #         return
    #     prev.next = temp.next
    #     temp = None

    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            temp = temp.next
            count += 1
        print(count)

    def printLinkedList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    n = int(input())
    value = list(map(int, input().split()))
    list = LinkedList()
    for i in value:
        list.AtEnd(i)
    list.getCount()
    list.printLinkedList()
