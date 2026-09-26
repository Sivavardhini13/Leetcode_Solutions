# Leetcode 1281 : Subtract the Product and Sum of Digits of an Integer
# Difficulty : Easy

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_sum=0
        digit_prod=1
        while n>0:
            digit_sum+=n%10
            digit_prod*=n%10
            n//=10
        return digit_prod - digit_sum