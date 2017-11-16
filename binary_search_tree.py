from tree_utilities import TreeNode

class BinarySearchTree(object):
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

    def monotonic(self, p, L):
        if not p:
            return True
        if not self.monotonic(p.left, L):
            return False
        if L[0] is not None and L[0].val > p.val:
            return False
        L[0] = p
        return self.monotonic(p.right, L)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        root = None
        if n > 0:
            middle = n/2
            root = TreeNode(nums[middle])
            root.left = self.sortedArrayToBST(nums[:middle])
            root.right = self.sortedArrayToBST(nums[middle+1:])
        return root

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # return self.isValidBST_1(root)
        return self.isThisValidBST(root, None, None)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.sortedArrayToBST([1,2,3,4])


