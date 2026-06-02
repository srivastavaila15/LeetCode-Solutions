# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        current = head        
        cycle = set()
        while current:
            if current in cycle:
                return current
            cycle.add(current)
            current = current.next
        return None
        


        