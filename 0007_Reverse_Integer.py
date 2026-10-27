# Leetcode Problem 7 : Reverse Integer
# Difficulty : Medium

class Solution:
    def reverse(self, x: int) -> int:
        # Remainder Approach
        rev=0
        sign=-1 if x<0 else 1
        x=abs(x)

        while x!=0:
            digit=x%10
            x//=10
            rev=rev*10+digit

        rev*=sign

        if rev<-(2**31) or rev>2**31-1:
            return 0

        return rev

        '''
        # String Approach
        temp=str(x)
        if x>=0:
            rev=int(temp[::-1])
        else:
            rev=-int(temp[:0:-1])

        if rev<-2**31 or rev>2**31-1:
            return 0
            
        return rev
        '''