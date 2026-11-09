# Leetcode 4106 : Find Mismatched Segments Between Two Strings
# Difficulty: Medium

class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res=[]
        start=-1
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if start==-1:
                    start=i
            elif start!=-1:
                res.append([s1[start:i],s2[start:i]])
                start=-1
        if start!=-1:
            res.append([s1[start:],s2[start:]])
        return res