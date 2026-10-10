class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        exist = set()
        same = False
        for i in s:
            if i not in t:
                if t.count(i) != s.count(i):
                    return False
        return True
            
        