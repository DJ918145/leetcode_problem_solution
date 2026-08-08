# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        return self.check(root, 0, targetSum)

    def check(self, node, ts, targetSum):
        ts += node.val

        # Leaf node
        if node.left is None and node.right is None:
            return ts == targetSum

        # Check left subtree
        if node.left is not None:
            if self.check(node.left, ts, targetSum):
                return True

        # Check right subtree
        if node.right is not None:
            if self.check(node.right, ts, targetSum):
                return True

        return False