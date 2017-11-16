from tree_utilities import TreeNode


class ConstructFromPreInorder(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = None
        if len(inorder) > 0:
            node = preorder.pop(0)
            root = TreeNode(node)
            p = inorder.index(node)
            left_side = inorder[:p]
            right_side = inorder[p + 1:]
            root.left = self.buildTree(preorder, left_side)
            root.right = self.buildTree(preorder, right_side)
        return root


if __name__ == '__main__':
    pre = [25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]
    ino = [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90]
    cfpi = ConstructFromPreInorder()
    cfpi.buildTree(pre, ino)
