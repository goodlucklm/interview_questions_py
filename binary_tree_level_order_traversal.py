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

    def bottomUPTraversal(self, root):
        results = []
        level = [root]
        while len(level) > 0:
            nodes = [node.val for node in level if node is not None]
            if len(nodes) > 0:
                results.insert(0, nodes)
            n = len(level)
            for i in range(n):
                node = level[i]
                if node is not None:
                    level += [node.left, node.right]
            level = level[n:]
        return results


if __name__ == '__main__':
    import tree_utilities
    root = tree_utilities.deserialize('[3,9,20,null,null,15,7]')
    solution = BinaryTreeLevelOrderTraversal()
    print solution.bottomUPTraversal(root)