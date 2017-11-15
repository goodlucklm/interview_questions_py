class BinaryTreeZigzagLevelOrderTraversal(object):
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

if __name__ == '__main__':
    import tree_utilities
    root = tree_utilities.deserialize('[3,9,20,null,null,15,7]')
    btzlot = BinaryTreeZigzagLevelOrderTraversal()
    print btzlot.zigzagLevelOrder(root)