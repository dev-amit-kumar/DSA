class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getCount(self):
        # code here
        lentgh = 0
        node = self.head
        while (node):
            lentgh += 1
            node = node.next
        print(lentgh)


a = LinkedList()
a.head = Node(5)
a.head.next = Node(10)
a.head.next.next = Node(11)
a.head.next.next.next = Node(12)
a.getCount()


# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def AtEnd(self, newdata):
#         NewNode = Node(newdata)
#         if self.head is None:
#             self.head = NewNode
#             return
#         temp = self.head
#         while(temp.next):
#             temp = temp.next
#         temp.next=NewNode

#     def getCount(self):
#         temp = self.head
#         count = 0
#         while(temp):
#             temp = temp.next
#             count += 1
#         print(count)

# if __name__ == "__main__":
#     n = int(input())
#     value = list(map(int, input().split()))
#     list = LinkedList()
#     for i in value:
#         list.AtEnd(i)
#     list.getCount()
