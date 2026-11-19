# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode()
        temp = dummy
        carry = 0

        while l1 or l2:

            num1 = 0
            num2 = 0

            if l1:
                num1 = l1.val
                l1 = l1.next

            if l2:
                num2 = l2.val
                l2 = l2.next

            total = num1 + num2 + carry

            carry = total // 10
            digit = total % 10

            temp.next = ListNode(digit)
            temp = temp.next

        if carry:
            temp.next = ListNode(carry)

        return dummy.next