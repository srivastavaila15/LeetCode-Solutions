# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxPath = float('-inf')
        def traversal(curr):
            if not curr: return 0
            maxLeft = max(0, traversal(curr.left))
            maxRight = max(0, traversal(curr.right))
            maxCurr = curr.val + maxLeft + maxRight
            self.maxPath = max(self.maxPath, maxCurr)

            return curr.val + max(maxLeft, maxRight)
        
        traversal(root)
        return self.maxPath
        