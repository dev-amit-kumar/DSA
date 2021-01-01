class Create_Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNewNode(self, node):
        pass


if __name__ == "__main__":
    list = LinkedList()

    first_node = Create_Node(12)
    second_node = Create_Node(13)
    third_node = Create_Node(14)
    print(list.head)  # before
    list.head = first_node
    temp = list.head
    print(list.head.value)  # after
    list.head.next = second_node
    temp.next = second_node
    temp = temp.next
    list.head.next.next = third_node
    temp.next = third_node
    temp = temp.next
    list.head.next.next.next = 4th
    list.head.next.next.next.next = 5th
    list.head.next.next.next.next.next = 6th
    list.head.next.next.next.next.next.next = 7th
    list.head.next.next.next.next.next.next.next = 8th

    n = int(input())  # how many node u want to add
    for i in range(0, n):
        user_val = int(input("Enter the value"))
        # logic to create new node
        node = Create_Node(user_val)
        # logic to append this node to linked list
        if(list.head is None):
            list.head = node
            temp = list.head
        else:
            temp.next = node
            temp = temp.next
