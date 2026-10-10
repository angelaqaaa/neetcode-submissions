class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            s_count = Counter(s)
            t_count = Counter(t)
            return s_count == t_count
        return False
