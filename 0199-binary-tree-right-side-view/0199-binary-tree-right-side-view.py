# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        ans = []
        queue = deque([root])
        while queue:
            lvlArray = []
            lvlSize = len(queue)
            for i in range(lvlSize):
                curr = queue.popleft()
                if i == 0:
                    ans.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)                
        return ans



        