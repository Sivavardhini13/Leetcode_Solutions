# Leetcode 2094 : Finding 3-Digit Even Numbers
# Difficulty : Easy

from itertools import permutations
from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums=set()
        for a,b,c in permutations(digits,3):
            if a and c%2==0:
                nums.add(a*100+b*10+c)
        return sorted(nums)