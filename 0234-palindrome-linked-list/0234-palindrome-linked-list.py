# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow = fast= head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        firstList = head
        secondList = prev
        while secondList is not None:
            if firstList.val != secondList.val:
                return False
            firstList = firstList.next
            secondList = secondList.next
        return True


         
            
            



        

        