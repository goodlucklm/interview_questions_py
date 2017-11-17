class BinaryTree(object):
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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        depth = 0
        level = [root]
        results = []
        while len(level) > 0:
            values = []
            for node in level:
                if node is not None:
                    values.append(node.val)
            if len(values) > 0:
                if depth % 2 != 0:
                    values.reverse()
                results.append(values)

            n = len(level)
            for i in range(n):
                node = level.pop(0)
                if node is not None:
                    level.append(node.left)
                    level.append(node.right)
            depth += 1
        return results

    def __get_height(self, root):
        if root is None:
            return 0
        else:
            return 1+max(self.__get_height(root.left), self.__get_height(root.right))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return abs(self.__get_height(root.left)-self.__get_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)



if __name__ == '__main__':
    import tree_utilities
    root = tree_utilities.deserialize('[3,9,20,null,null,15,7]')
    solution = BinaryTree()
    print solution.bottomUPTraversal(root)