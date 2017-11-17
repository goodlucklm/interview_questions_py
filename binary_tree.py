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
        if not root: return 0
        d = map(self.minDepth, (root.left, root.right))
        return 1 + (min(d) or max(d))

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

    def __find_path_sum(self, root, sum, path, results):
        if root is not None:
            path.append(root.val)
            if root.left is None and root.right is None and sum == root.val:
                results.append(path)
            else:
                self.__find_path_sum(root.left, sum-root.val, path, results)
                self.__find_path_sum(root.right, sum-root.val, path, results)
            path.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        self.__find_path_sum(root, sum, [], results)
        return results

    def __preorder_flatten(self, root, st):
        if root is not None:
            st.append(root)
            self.__preorder_flatten(root.left, st)
            self.__preorder_flatten(root.right, st)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None or (root.left is None and root.right is None): return
        st = []
        self.__preorder_flatten(root, st)
        n = root
        for i in range(1, len(st)):
            n.left = None
            n.right = st[i]
            n = st[i]
        return None

    def iterative_flatten(self, root):
        while root is not None:
            if root.left is not None:
                left_node = root.left
                while left_node.right is not None:
                    left_node = left_node.right
                left_node.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


if __name__ == '__main__':
    import tree_utilities

    root = tree_utilities.deserialize('[1,2]')
    solution = BinaryTree()
    print solution.iterative_flatten(root)
