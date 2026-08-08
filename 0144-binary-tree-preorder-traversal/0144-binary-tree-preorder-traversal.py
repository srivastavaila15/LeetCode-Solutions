# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        res = []

        def traversal(curr):
            if not curr: return
            res.append(curr.val)
            traversal(curr.left)
            traversal(curr.right)
        traversal(root)
        return res
        