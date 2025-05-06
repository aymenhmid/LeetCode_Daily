#06-05-2025
#O(n) space
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in  range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
  #O(1) space
  class Solution(object):
    def buildArray(self, nums):
        for i in range(len(nums)):
            nums[i] += (1024 * (nums[nums[i]] % 1024))
        
        for i in range(len(nums)):
            nums[i] //= 1024
        
        return nums
