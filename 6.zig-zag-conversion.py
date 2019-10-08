#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start


class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    rows = [''] * numRows
    y = 0
    f = 1
    for i in range(len(s)):
      rows[y] += s[i]
      y = y + f
      if y == numRows - 1:
        f = -1
      elif y == 0:
        f = 1
    return ''.join(rows)
# @lc code=end


# sol = Solution()
# assert(sol.convert('AB', 1) == 'AB')
# assert(sol.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
# assert(sol.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')
