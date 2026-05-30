# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        cycle = set()
        current = head
        while current:
            if current in cycle:
                return True
            cycle.add(current)
            current = current.next
        return False
        