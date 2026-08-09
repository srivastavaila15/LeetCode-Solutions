# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        self.ans = True
        def calculateHeight(curr):
            
            if not curr: return 0

            leftHeight = calculateHeight(curr.left)
            rightHeight = calculateHeight(curr.right)
            if abs(leftHeight - rightHeight) > 1:
                self.ans = False
            return 1 + max(leftHeight, rightHeight)
        calculateHeight(root)
        return self.ans
        
        