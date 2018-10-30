# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        sum = l1.val + l2.val
        rlt = ListNode(0)
        if sum <10:
            rlt.val = sum
            rlt.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            rlt.val = sum -10
            rlt.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
        return rlt