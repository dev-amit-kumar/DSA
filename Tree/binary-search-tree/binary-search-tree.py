class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insertValue(self, data):
        NewNode = Node(data)
        if self.root is None:
            self.root = NewNode
            return
        cur_node = self.root
        while True:
            if data < cur_node.data:
                if cur_node.left is not None:
                    cur_node = cur_node.left
                else:
                    cur_node.left = NewNode
                    break
            elif data >= cur_node.data:
                if cur_node.right is not None:
                    cur_node = cur_node.right
                else:
                    cur_node.right = NewNode
                    break

    def printBST(self):
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


if __name__ == "__main__":
    tree = BST()
    arr = [5, 4, 7, 1, 2, 8, 6]
    for i in arr:
        tree.insertValue(i)
    tree.printBST()
