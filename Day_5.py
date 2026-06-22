"""
# Day 5: Product of Array Except Self

**LeetCode 238 (Medium)**

## Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

**Note:** You must write an algorithm that runs in $O(n)$ time and without using the division operation.

**Example 1:**
Input: nums = [1,2,3,4]
Output: [24,12,8,6]"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n
        
        # Pass 1: Calculate prefix products
        # prefix represents the product of all elements to the left of i 
        prefix = 1
        for i in range(n):
            result[i] = prefix 
            prefix *= nums[i]
            
        # Pass 2: Calculate postfix products and multiply with prefix
        # postfix represents the product of all elements to the right of i
        postfix = 1
        for i in range(n - 1, -1, -1):
            # Multiply the left product (already in result) by the right product
            result[i] *= postfix
            # Update the right product for the next person in line
            postfix *= nums[i]
            
        return result