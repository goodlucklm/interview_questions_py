# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recover(self, p, prev):
        if p is not None:
            self.recover(p.left, prev)
            if prev[0] is not None and prev[0].val > p.val:
                tmp = prev[0].val
                prev[0].val = p.val
                p.val = tmp
                return True
            prev[0] = p
            self.recover(p.right, prev)
        return False

    def find_misplaced_nodes(self, p, nodes, prev):
        if p is not None:
            self.find_misplaced_nodes(p.left, nodes, prev)
            if prev[0] is not None and prev[0].val > p.val:
                if nodes[0] is None:
                    nodes[0] = prev[0]
                else:
                    nodes[1] = p
            prev[0] = p
            self.find_misplaced_nodes(p.right, nodes, prev)
            return nodes


    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        L = self.find_misplaced_nodes(root, [None, None], [None])
        tmp = L[0].val
        L[0].val = L[1].val
        L[1].val = tmp
