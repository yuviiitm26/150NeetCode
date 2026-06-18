"""238. Product of Array Except Self

Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n
        
        #pass 1: calculate prefix products
        # prefix represents the product of all elements to the left of i 
        prefix = 1
        for i in range(n):
            result[i] = prefix 
            prefix *= nums[i]
        # pass 2 : Calculate postfix products and multiply with prefix
        # postfix represents the product of all elements to the right of i
        postfix = 1
        for i in range(n-1, -1, -1):
            # multiply the left product already in result) by the right product
            result[i] *=postfix
            # update the right product for the next person in line
            postfix *= nums[i]
        return result 
