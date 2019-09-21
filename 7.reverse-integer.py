#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


class Solution:
    def reverse(self, x: int) -> int:
        if x < -pow(2, 31) or x > pow(2, 31) - 1:
            return 0
        r = []
        k = 1
        if x < 0:
            k = -1
            x = -x
        s = False
        for i in range(10, 0, -1):
            f = pow(10, i)
            if x >= f or s:
                d = x // f
                x = x - f * d
                s = True
                r.append(d)
        r.append(x)

        t = 0
        for i in range(len(r)):
            t = t + r[i] * pow(10, i)

        t = t * k
        if t < -pow(2, 31) or t > pow(2, 31) - 1:
            return 0
        return t


s = Solution()
