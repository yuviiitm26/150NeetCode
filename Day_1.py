#217. Contains Duplicate

# Easy
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#solution :  from scratch

class MyHashSet:
  def __init__(self, size=1000):
    self.size = size
    #Initialize buckets as a list of empty lists
    self.buckets = [[] for _ in range(self.size)]

  def _hash(self, key):
    return key % self.size

  def add(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]
    if key not in bucket:
      bucket.append(key)

  def remove(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]
    if key not in bucket:
      bucket.append(key)

  def contains(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]
    return key in bucket

class Solution:
  def containsDuplicate(self, nums):
    #Intialize mine custom hast set
    my_set = MyHashSet()

    for num in nums:
      #if my set already contains the number, it's a duplicate
      if my_set.contains(num):
        return True

      #otherwise, add the number to my set
      my_set.add(num)

    #if finishes without returning, all elements are distinct
    return False
#solution : using built in set
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Initialize mine custom hash set
        my_set = set()

        #loop through the array
        for num in nums:
            if num in my_set:
                return True
            #otherwise , add the number to my set
            my_set.add(num)

        # if the loop finishes without returning, all elements are distinct
        return False