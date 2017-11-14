# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def retrieve_values(self, p, pool, m):
        if not p:
            return m
        if p.val in pool:
            pool[p.val] += 1
            m = max(pool[p.val], m)
        else:
            pool[p.val] = 1
            m = max(pool[p.val], m)
        m = max(m, self.retrieve_values(p.left, pool, m))
        m = max(m, self.retrieve_values(p.right, pool, m))
        return m


    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = dict()
        r = []
        m = self.retrieve_values(root, results, 0)
        for k in results.keys():
            if results[k] == m:
                r.append(k)
        return r


