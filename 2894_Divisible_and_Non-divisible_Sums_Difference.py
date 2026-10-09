# Leetcode 2894 : Divisible and Non-divisible Sums Difference
# Difficulty : Easy

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div=0
        non_div=0
        for i in range(1,n+1):
            if i%m==0:
                div+=i
            else:
                non_div+=i
        return non_div-div

        '''
        # using AP formula
        tot_sum=n*(n+1)//2
        div_count=n//m
        div_sum=m*div_count*(div_count+1)//2
        return tot_sum-2*div_sum
        '''