class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.result = []
        self.find_route(root, '')
        return self.result

    def find_route(self, root, all_route):
        if root is None:
            return None
        if not root.left and not root.right:
            self.result.append(all_route + str(root.val))
        self.find_route(root.left, all_route + str(root.val) + '->')
        self.find_route(root.right, all_route + str(root.val)+ '->' )