class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0:
            return False

        symbols = ['()', '[]', '{}', ',', ':', '.', ';', '@', '=', '->', '?', ' ', "'"]
        # remove the unessary symbol
        only_string = ""

        for char in s.lower():
            if char not in symbols:
                only_string+=char

        is_palindrome = True

        left = 0
        right = len(only_string)-1

        while left < right:
            
            if only_string[left] != only_string[right]:
                return False
            else:
                left+=1
                right-=1
        
        return True

            







        