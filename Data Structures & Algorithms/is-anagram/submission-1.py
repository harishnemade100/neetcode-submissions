class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False

        char_frq = {}

        for i in s:
            if i in char_frq:
                char_frq[i]+=1
            else:
                char_frq[i]=1
        
        for char in t:
            if char not in char_frq:
                return False
            
            char_frq[char]-=1
            if char_frq[char]<0:
                return False
        
        return True