# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ans = ListNode()
        ansHead = ans
        while(l1 or l2 or carry):
            add = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = add/10
            digit = add%10

            newNode = ListNode(digit)
            ans.next = newNode
            ans = ans.next

            l1 = l1 and l1.next
            l2 = l2 and l2.next
        
        return ansHead.next
