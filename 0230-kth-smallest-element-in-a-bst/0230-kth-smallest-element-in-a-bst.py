# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.ans = None
        self.count = k
        def traversal(curr):
            if not curr:
                return

            traversal(curr.left)
            self.count -= 1
            if self.count == 0:
                self.ans = curr.val
            traversal(curr.right)
        
        traversal(root)
        return self.ans
        