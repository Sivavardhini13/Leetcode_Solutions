# Leetcode 2544 : Alternating Digit Sum
# Difficulty: Easy

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum,i=0,0
        while n!=0:
            if i%2==0:
                sum+=n%10
            else:
                sum-=n%10
            i+=1
            n//=10
        if i%2==0:
            return 0-sum
        return sum

        '''
        # String Conversion
        s=str(n)
        ans=0
        for i in range(0,len(s),2):
            ans+=int(s[i])
        for i in range(1,len(s),2):
            ans-=int(s[i])
        return ans
        '''