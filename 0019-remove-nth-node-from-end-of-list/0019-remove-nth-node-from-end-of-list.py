# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummyNode = ListNode(0)
        dummyNode.next = head
        length = 0
        while head:
            head = head.next
            length += 1
        prevPos = length - n
        print(prevPos)
        prev = dummyNode
        for i in range(prevPos):
            prev = prev.next
        prev.next = prev.next.next
        return dummyNode.next
        