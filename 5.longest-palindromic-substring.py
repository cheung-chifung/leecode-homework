#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


class Solution:
  def longestPalindrome(self, s: str) -> str:
    if len(s) == 0:
      return ""

    n = len(s)
    D = [["" for x in range(n)] for x in range(n)]
    for i in range(n):
      D[i][i] = s[i]

    for cl in range(2, n+1):
      for i in range(n-cl+1):
        j = i + cl - 1
        if s[i] == s[j] and cl == 2:
          D[i][j] = s[i:j+1]
        elif s[i] == s[j] and D[i+1][j-1] == s[i+1:j]:
          D[i][j] = s[i] + D[i+1][j-1] + s[j]
        else:
          if len(D[i+1][j]) > len(D[i][j-1]):
            D[i][j] = D[i+1][j]
          else:
            D[i][j] = D[i][j-1]
    # for i in range(n):
    #   for j in range(n):
    #     print(i, j, D[i][j])
    # print(D[0][n-1])
    return D[0][n-1]


# sol = Solution()
# assert sol.longestPalindrome("") in [""]
# assert sol.longestPalindrome("a") in ["a"]
# assert sol.longestPalindrome("babad") in ["bab", "aba"]
# assert sol.longestPalindrome("ggabad") in ["aba"]
# assert sol.longestPalindrome("cbbd") in ["bb"]
# assert sol.longestPalindrome("ba121ab") in ["ba121ab"]
# assert sol.longestPalindrome("ba1121ab") in ["121"]
