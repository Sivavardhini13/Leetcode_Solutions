# Leetcode 2119 : A Number After a Double Reversal
# Difficulty : Easy

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num==0 or num%10!=0

        '''
        # String Conversion
        rev1=int(str(num)[::-1])
        rev2=int(str(rev1)[::-1])
        return rev2==num
        '''