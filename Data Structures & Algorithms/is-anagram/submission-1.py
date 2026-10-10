class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            anagrams = []
            for i in s:
                if i in t:
                    anagrams.append(t.count(i) == s.count(i))
                else: 
                    return False      
            if all(anagrams) == True:
                return True
            else: 
                return False
        return False
            
        