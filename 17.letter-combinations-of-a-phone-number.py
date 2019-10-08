#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


class Solution:
  def letterCombinations(self, digits: str):
    m = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    if len(digits) == 0:
      return []

    if len(digits) == 1:
      d = digits[0]
      return list(m[d])

    prev = self.letterCombinations(digits[:-1])
    return [p + d for p in prev for d in m[digits[-1]]]


# sol = Solution()
# assert(sol.letterCombinations("23") == [
#        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
