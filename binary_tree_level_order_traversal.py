class BinaryTreeLevelOrderTraversal(object):
    def traverse(self, p, results, depth):
        if p is not None:
            self.traverse(p.left, results, depth+1)
            while len(results) <= depth:
                results.append([])
            results[depth].append(p.val)
            self.traverse(p.right, results, depth+1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = []
        self.traverse(root, results, 0)
        return results

if __name__ == '__main__':
    import tree_utilities
    root = tree_utilities.deserialize('[3,9,20,null,null,15,7]')
    solution = BinaryTreeLevelOrderTraversal()
    print solution.levelOrder(root)