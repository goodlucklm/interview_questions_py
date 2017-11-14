

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return self.isSameTree(p.left, q.left) and p.val == q.val and self.isSameTree(p.right, q.right)
