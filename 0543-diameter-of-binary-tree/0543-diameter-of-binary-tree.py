# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def findDepth(curr):
            
            if not curr:
                return 0
            leftDepth = findDepth(curr.left)
            rightDepth = findDepth(curr.right)
            currDiameter = leftDepth + rightDepth
            self.diameter = max(currDiameter, self.diameter)
            return 1 + max(leftDepth, rightDepth)
        
        findDepth(root)
        return self.diameter

        
        
        