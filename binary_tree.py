class BinaryTree(object):
    def traverse(self, p, results, depth):
        if p is not None:
            self.traverse(p.left, results, depth + 1)
            while len(results) <= depth:
                results.append([])
            results[depth].append(p.val)
            self.traverse(p.right, results, depth + 1)

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
            return 1 + max(self.__get_height(root.left), self.__get_height(root.right))

    def __get_dfs_height(self, root):
        if root is None:
            return 0
        left_height = self.__get_dfs_height(root.left)
        if left_height == -1:
            return -1
        right_height = self.__get_dfs_height(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if root is None:
        #     return True
        # return abs(self.__get_height(root.left)-self.__get_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        return self.__get_dfs_height(root) != -1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is None:
            return 1+self.minDepth(root.left)
        elif root.right is not None and root.left is None:
            return 1+self.minDepth(root.right)
        else:
            return 1+min(self.minDepth(root.left), self.minDepth(root.right))

if __name__ == '__main__':
    import tree_utilities

    root = tree_utilities.deserialize('[1,2,3,4,5]')
    solution = BinaryTree()
    print solution.minDepth(root)