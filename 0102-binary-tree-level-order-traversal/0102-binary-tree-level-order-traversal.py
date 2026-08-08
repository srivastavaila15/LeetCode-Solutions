# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        queue = deque()
        queue = [root]
        ans = []
        while len(queue):
            lvlArr = []
            lvlSize = len(queue)
            for i in range(lvlSize):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                lvlArr.append(curr.val)
            ans.append(lvlArr)
        return ans
        