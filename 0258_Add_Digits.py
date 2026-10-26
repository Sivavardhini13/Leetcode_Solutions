# Leetcode 258 : Add Digits
# Difficulty : Easy

class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        return 1+(num-1)%9

    '''
        if num<=9:
            return num
        while num>9:
            digit=0
            while num>0:
                digit+=num%10
                num//=10
            num=digit
        return num
    '''
