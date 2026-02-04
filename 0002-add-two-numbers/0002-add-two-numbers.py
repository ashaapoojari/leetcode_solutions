class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = tail = ListNode(0)

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            s = a + b + carry
            carry = s // 10

            tail.next = ListNode(s % 10)
            tail = tail.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head.next
