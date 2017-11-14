# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ValidBinarySearchTree(object):
    def areAllNodesLessThan(self, p, val):
        if not p:
            return True
        return p.val < val and self.areAllNodesLessThan(p.left, val) and self.areAllNodesLessThan(p.right, val)

    def areAllNodesGreaterThan(self, p, val):
        if not p:
            return True
        return p.val > val and self.areAllNodesGreaterThan(p.left, val) and self.areAllNodesGreaterThan(p.right, val)

    def isValidBST_1(self, root):
        if not root:
            return True
        return self.areAllNodesLessThan(root.left, root.val) and self.areAllNodesGreaterThan(root.right, root.val) and self.isValidBST(root.left) and self.isValidBST(root.right)

    def isThisValidBST(self, p, lower, upper):
        if not p:
            return True
        return (lower is None or p.val > lower) and (upper is None or p.val < upper) and \
               self.isThisValidBST(p.left, lower, p.val) and self.isThisValidBST(p.right, p.val, upper)


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # return self.isValidBST_1(root)
        return self.isThisValidBST(root, None, None)