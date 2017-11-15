class SymmetricTree(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        level = [root]
        while len(level) > 0:
            values = []
            for node in level:
                if node is None:
                    values.append(None)
                else:
                    values.append(node.val)
            for i in range(len(values)/2):
                if values[i] != values[-1*(i+1)]:
                    return False
            n = len(level)
            for i in range(n):
                node = level.pop(0)
                if node is not None:
                    level.append(node.left)
                    level.append(node.right)

        return True

if __name__ == '__main__':
    import tree_utilities
    root = tree_utilities.deserialize('[1,2,2,null,3,null,3]')
    st = SymmetricTree()
    print st.isSymmetric(root)

