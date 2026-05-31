# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummyNode = ListNode(0)
        dummyNode.next = head
        dummySet = set()
        prev = dummyNode
        while(prev and prev.next):
            if(prev.next.val not in dummySet):
                dummySet.add(prev.next.val)
                prev = prev.next
            else:
                prev.next = prev.next.next
        return head
        