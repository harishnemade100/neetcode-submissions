class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:  # if it's a closing bracket
                if stack and stack[-1] == mapping[char]:
                    stack.pop()   # valid pair, remove from stack
                else:
                    return False  # invalid
            else:
                stack.append(char)  # opening bracket, push to stack

        return not stack  # stack should be empty if valid