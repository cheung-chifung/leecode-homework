#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = []
        idx = 0
        for i in range(len(str)):
            for j in range(len(s)):
                print([i, j])
