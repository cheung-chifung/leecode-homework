#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        last = None
        inc = 0
        while True:
            n1 = 0
            if l1 is not None:
                n1 = l1.val
            n2 = 0
            if l2 is not None:
                n2 = l2.val
            d = (n1 + n2 + inc) % 10
            nn = ListNode(d)
            if res is None:
                res = nn
            if last is not None:
                last.next = nn

            last = nn

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            if (n1 + n2 + inc) >= 10:
                inc = 1
            else:
                inc = 0

            if l1 is None and l2 is None and inc == 0:
                break

        return res
