class MaximumDepthOfBinaryTree(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if root is None else 1+max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    import tree_utilities
    mdobt = MaximumDepthOfBinaryTree()
    root = tree_utilities.deserialize('[3,9,20,null,null,15,7]')
    print mdobt.maxDepth(root)
