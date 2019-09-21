#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


class Solution:
  def myAtoi(self, s: str) -> int:
    ans = 0
    s = s.strip()
    start = 0
    sign = 1
    if not s:
      return 0

    if s[0] == '-':
      sign = -1
      start = 1
    elif s[0] == '+':
      start = 1
    elif not s[0].isdigit():
      return 0

    for char in s[start:]:
      if not char.isdigit():
        break
      ans = ans * 10 + int(char)

    ans *= sign
    ans = max(ans, - 2**31)
    ans = min(ans, 2**31 - 1)
    # print(ans)
    return ans


sol = Solution()
assert sol.myAtoi("+42") == 42
assert sol.myAtoi("+-42") == 0
assert sol.myAtoi("42") == 42
assert sol.myAtoi("   -42") == -42
assert sol.myAtoi("4193 with words") == 4193
assert sol.myAtoi("words and 987") == 0
assert sol.myAtoi("-91283472332") == -2147483648
assert sol.myAtoi("3.14159") == 3
assert sol.myAtoi("   +0 123") == 0
