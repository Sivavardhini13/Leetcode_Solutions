# Leetcode 678 : Valid Parenthesis String
# Difficulty : Medium

class Solution:
    def checkValidString(self, s: str) -> bool:
        low=high=0

        for c in s:
            if c =='(':
                low+=1
                high+=1

            elif c==')':
                low-=1
                high-=1

            else: # '*'
                low-=1
                high+=1

            if high<0:
                return False

            low=max(low,0)
            
        return low==0

    '''
        # Compact method using bitwise
        l=h=0
        for c in s:
            l+=((c=='(')<<1)-1
            h+=((c!=')')<<1)-1
            if h<0: return False
            l=max(l,0)
        return l==0
    '''