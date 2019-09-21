#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# Sliding window
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    i = j = 0
    ans = 0
    n = len(s)
    ss = set()
    while i < n and j < n:
      #   print("run", s[i: j], i, j, ss, ans)
      c = s[j]
      if c in ss:
        ss.remove(s[i])
        i = i + 1
      else:
        ss.add(c)
        j = j + 1
        ans = max(j-i, ans)
    return ans

# Brute Force
#
# class Solution:
#   def lengthOfLongestSubstring(self, s: str) -> int:
#     cstr = ""
#     l = 0
#     for i in range(len(s)):
#       for j in range(i, len(s)):
#         n = s[i:j+1]
#         uniq = list(set(list(n)))
#         if len(uniq) == len(n) and len(n) > l:
#           l = len(n)
#           cstr = n
#     return l


# sol = Solution()
# assert sol.lengthOfLongestSubstring("abcabcbb") == 3
# assert sol.lengthOfLongestSubstring("bbbbb") == 1
# assert sol.lengthOfLongestSubstring("pwwkew") == 3
# assert sol.lengthOfLongestSubstring("a") == 1
# assert sol.lengthOfLongestSubstring("au") == 2
