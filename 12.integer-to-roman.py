#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start


class Solution:
  def intToRoman(self, num: int) -> str:
    ans = ''
    if num >= 1000:
      d, num = num // 1000, num % 1000
      ans += 'M' * d
    if num >= 100:
      d, num = num // 100, num % 100
      if d < 4:
        ans += 'C' * d
      elif d == 4:
        ans += 'CD'
      elif d == 9:
        ans += 'CM'
      else:
        ans += 'D' + 'C' * (d - 5)
    if num >= 10:
      d, num = num // 10, num % 10
      if d < 4:
        ans += 'X' * d
      elif d == 4:
        ans += 'XL'
      elif d == 9:
        ans += 'XC'
      else:
        ans += 'L' + 'X' * (d - 5)
    if num >= 1:
      d = num
      if d < 4:
        ans += 'I' * d
      elif d == 4:
        ans += 'IV'
      elif d == 9:
        ans += 'IX'
      else:
        ans += 'V' + 'I' * (d - 5)
    return ans


# @lc code=end
sol = Solution()
assert(sol.intToRoman(3), 'III')
assert(sol.intToRoman(4), 'IV')
assert(sol.intToRoman(9), 'IX')
assert(sol.intToRoman(58), 'LVIII')
assert(sol.intToRoman(1994), 'MCMXCIV')
