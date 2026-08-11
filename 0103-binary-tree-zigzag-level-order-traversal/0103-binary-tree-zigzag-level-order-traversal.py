# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root: return []
        ans = []
        queue = deque([root])
        lvl = 0
        while len(queue):
            lvlArray = []
            lvlSize = len(queue)
            for i in range(lvlSize):
                curr = queue.popleft()
                if lvl%2 == 0:
                    lvlArray.append(curr.val)
                else:
                    lvlArray.insert(0, curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            ans.append(lvlArray)
            lvl += 1
        return ans