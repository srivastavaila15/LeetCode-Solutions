# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val #to copy the next value to node
        node.next = node.next.next # to bypass the node value

        
        
        