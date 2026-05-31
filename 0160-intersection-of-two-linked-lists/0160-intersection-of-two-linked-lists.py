# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        current = headB
        currentA = headA
        setHeadB = set()
        while current:
            setHeadB.add(current)
            current = current.next
        while currentA:
            if currentA in setHeadB:
                return currentA
            currentA = currentA.next
        return None
            
        

        