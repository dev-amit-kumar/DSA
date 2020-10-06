class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Method to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)

        if self.head is None:
            self.head = NewNode
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = NewNode

    # Method to add the new nodes next val to existing node
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

    def Inbetween(self, middle_node, newdata):

        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    # Method to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal is None):
            return
        prev.next = HeadVal.next
        HeadVal = None

    # Print the linked list
    def listprint(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    n = int(input())
    value = list(map(int, input().split()))
    list = LinkedList()
    for i in value:
        list.AtEnd(i)

    list.listprint()
