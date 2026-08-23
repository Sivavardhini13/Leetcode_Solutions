# Leetcode : 49
# Difficulty : Medium

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in a:
                a[key]=[]
            a[key].append(word)
        return sorted([sorted(group) for group in a.values()])