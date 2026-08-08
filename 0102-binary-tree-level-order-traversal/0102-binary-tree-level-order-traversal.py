# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        ans = []
        
        def traversal(curr, level):
            if not curr: return
            if len(ans) == level: 
                ans.append([])
            ans[level].append(curr.val)
            if curr.left:
                traversal(curr.left, level+1)
            if curr.right:
                traversal(curr.right, level+1)
        traversal(root, 0)
        return ans


        