# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        self.ans = None
        def traversal(curr):
            if curr.val == val:
                self.ans = curr
            else:
                if curr.val < val:
                    if curr.right: traversal(curr.right)
                else:
                    if curr.left: traversal(curr.left)
        traversal(root)
        return self.ans

        