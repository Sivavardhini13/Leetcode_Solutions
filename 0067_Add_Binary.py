# Leetcode 67 : Add Binary
# Difficulty : Easy

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=list(a),list(b)
        carry=0
        res=[]
        while a or b or carry:
            tot=carry
            if a:
                tot+=int(a.pop())
            if b:
                tot+=int(b.pop())
            res.append(str(tot%2))
            carry=tot//2
        return "".join(reversed(res))

        '''
        # Built-in conversion approach
        return bin(int(a,2)+int(b,2))[2:]
        '''