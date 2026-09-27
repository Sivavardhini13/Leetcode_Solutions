# Leetcode 509 : Fibonacci Number
# Difficulty : Easy

class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        for i in range(n):
            a,b=b,a+b
        return a