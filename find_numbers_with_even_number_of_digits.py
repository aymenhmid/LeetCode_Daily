#method1 : convert to string and get length
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                sum += 1
        return sum
#method 2 : use math module
import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            x = math.floor(math.log10(abs(num))) + 1
            if x % 2 == 0 :
                sum += 1
        return sum
#method 3  : bit manipulation
class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            msb = i.bit_length() - 1
            digits = int(msb * 0.30103) + 1
            if i >= 10**digits:
                digits += 1
            if digits % 2 == 0:
                count += 1
        return count
