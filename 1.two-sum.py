#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


class Solution:
  def twoSum(self, nums, target):
    m = {}
    for i in range(len(nums)):
      r = (target - nums[i])
      if r in m:
        return [m[r], i]
      m[nums[i]] = i
    return []


sol = Solution()
assert(sol.twoSum([2, 7, 11, 15], 9) == [0, 1])
assert(sol.twoSum([3, 2, 4], 6) == [1, 2])


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
