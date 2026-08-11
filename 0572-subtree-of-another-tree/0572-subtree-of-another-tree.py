# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        hashRt = self.serialize(root)
        hashSbRt = self.serialize(subRoot)
        return hashSbRt in hashRt
    
    
    def serialize(self, root):
        self.hashRoot = ""
        def traversal(curr):
            if not curr:
                self.hashRoot = self.hashRoot + "-#"
                return

            self.hashRoot = self.hashRoot + "-" + str(curr.val)
            traversal(curr.left)
            traversal(curr.right)
        
        traversal(root)
        return self.hashRoot
        