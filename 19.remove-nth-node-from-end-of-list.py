#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
import collections


class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    node = head
    q = collections.deque()
    l = 1
    while (True):
      q.appendleft(node)
      if len(q) > n + 1:
        q.pop()

      if node.next:
        node = node.next
        l += 1
      else:
        if l == n:
          return head.next
        else:
          np1th = q.pop()
          if np1th.next:
            nth = np1th.next
            np1th.next = None
            if nth and nth.next:
              np1th.next = nth.next
        return head
# @lc code=end


# def appendToListNode(v, last):
#   node = ListNode(v)
#   if len(last) > 0:
#     node.next = appendToListNode(last[0], last[1:])
#   return node


# def toListNode(arr):
#   return appendToListNode(arr[0], arr[1:])


# def printListNode(head):
#   if head:
#     print(head.val)
#     printListNode(head.next)


# sol = Solution()
# ans = sol.removeNthFromEnd(toListNode([1, 2, 3, 4, 5]), 2)
# printListNode(ans)
# ans = sol.removeNthFromEnd(toListNode([1]), 1)
# ans = sol.removeNthFromEnd(toListNode([1, 2]), 1)
# ans = sol.removeNthFromEnd(toListNode([1, 2, 3]), 2)
# printListNode(ans)
# nl = toListNode([1, 2, 3, 4, 5])
# printListNode(nl)
