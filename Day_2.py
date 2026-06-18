#2 Two Sum #Easy

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
  def twosum(self, nums, target):
    n=lens(nums)
    nummap = {}
    for i in range(n):
      complement = target - nums[i]
      if complement in nummap:
        return [i, nummap[complement]]
      nummap[nums[i]] = i
    return []