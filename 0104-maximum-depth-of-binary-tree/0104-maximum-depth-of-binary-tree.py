# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        self.maxDep = 0
        def traversal(curr, depth):
            self.maxDep = max(self.maxDep, depth)
            if not curr: return
            if curr.left:
                traversal(curr.left, depth+1)
            if curr.right:
                traversal(curr.right, depth+1)
        traversal(root, 1)
        return self.maxDep
        