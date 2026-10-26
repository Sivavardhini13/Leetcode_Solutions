# Leetcode 728 : Self Dividing Numbers
# Difficulty: Easy

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res=[]
        for i in range(left, right+1):
            temp=i
            while temp!=0:    
                digit=temp%10
                if digit==0 or i%digit!=0:
                    break
                temp//=10
            if temp==0:
                res.append(i)
        return res