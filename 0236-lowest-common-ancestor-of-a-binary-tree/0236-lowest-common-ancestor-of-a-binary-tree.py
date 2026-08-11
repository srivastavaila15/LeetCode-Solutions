# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        self.lca = None
        def traversal(curr):
            count = 0
            if not curr: return 0

            ansLeft = traversal(curr.left)
            ansRight = traversal(curr.right)
            count = count + ansLeft + ansRight
            if curr == p or curr == q:
                count = count + 1
            
            if count == 2 and not self.lca:
                self.lca = curr
            return count
        traversal(root)
        return self.lca
        