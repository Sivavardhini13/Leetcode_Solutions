# Leetcode 3945 : Digit Frequency Score
# Difficulty : Easy

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(d) for d in str(n))
        
        '''
        # Digit Extraction Method
        sum=0
        while n>0:
            sum+=n%10
            n//=10
        return sum
        '''