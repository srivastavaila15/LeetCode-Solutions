# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def traversal(curr, low, high):
            if not curr: return True
            if low is not None and curr.val <= low: return False
            if high is not None and curr.val >= high: return False

            return traversal(curr.left, low, curr.val) and traversal(curr.right, curr.val, high)

        return traversal(root, None, None)
        