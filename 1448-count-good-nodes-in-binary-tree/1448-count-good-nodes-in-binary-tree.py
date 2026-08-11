# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        self.count = 0
        def traversal(curr, maxSeen):
            if curr.val >= maxSeen:
                self.count += 1
            curr_count = max(maxSeen, curr.val)
            if curr.left:
                traversal(curr.left, curr_count)
            if curr.right:
                traversal(curr.right, curr_count)
            return self.count

        traversal(root, float('-inf'))
        return self.count