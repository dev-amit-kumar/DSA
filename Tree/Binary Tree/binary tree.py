class Node:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None


class binaryTree:
    def __init__(self):
        self.root = None

    def insertValue(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        tree = []
        tree.append(self.root)
        while len(tree):
            temp = tree[0]
            tree.pop(0)
            if (temp.left is None):
                temp.left = newNode
                break
            else:
                tree.append(temp.left)
            if (temp.right is None):
                temp.right = newNode
                break
            else:
                tree.append(temp.right)

    def printLevelOrder(self):
        tree = []
        tree.append(self.root)
        while len(tree):
            temp = tree[0]
            if temp is None:
                return
            print(temp.data)
            tree.pop(0)
            tree.append(temp.left)
            tree.append(temp.right)

    def LeftView(self):
        tree = []
        tree.append(self.root)
        while len(tree):
            temp = tree[0]
            tree.pop(0)
            if temp is None:
                return
            print(temp.data, end="")
            tree.append(temp.left)


if __name__ == "__main__":
    tree = binaryTree()
    # arr = list(map(int, input().split()))
    arr = [1, 2, 3, 4, 5]
    for i in arr:
        tree.insertValue(i)
    tree.printLevelOrder()
    tree.LeftView()
