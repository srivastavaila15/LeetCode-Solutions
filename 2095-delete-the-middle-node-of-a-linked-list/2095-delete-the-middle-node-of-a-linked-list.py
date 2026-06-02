# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        newNode = ListNode()
        slow = newNode
        #slow = head
        fast = head
        newNode.next = head
        current = head
        if head.next is None: return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #prev = prev.next
        slow.next = slow.next.next
        return head
        
        
        
        
        