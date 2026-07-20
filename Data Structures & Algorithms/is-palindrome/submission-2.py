class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alpha_symbol = ["/",".",",",":","?"," ","'"]

        pre_string = ""

        for elemant in s:
            if elemant not in alpha_symbol:
                pre_string+=elemant.lower()

        left = 0
        right = len(pre_string)-1

        is_palindrome = True
        while left < right:
            if pre_string[left] != pre_string[right]:
                is_palindrome = False
                break
            else:
                left +=1
                right -=1
        
        if is_palindrome:
            return True
        else:
            return False


