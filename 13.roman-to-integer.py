#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start


class Solution:
  def romanToInt(self, s: str) -> int:
    ans = 0
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    mm = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }
    i = 0
    while (i < len(s)):
      if s[i:i+2] in mm:
        ans += mm[s[i:i+2]]
        i += 2
      elif s[i] in m:
        ans += m[s[i]]
        i += 1
      else:
        i += 1
    return ans
# @lc code=end


sol = Solution()
assert(sol.romanToInt('III') == 3)
assert(sol.romanToInt('IV') == 4)
assert(sol.romanToInt('IX') == 9)
assert(sol.romanToInt('LVIII') == 58)
assert(sol.romanToInt('MCMXCIV') == 1994)
