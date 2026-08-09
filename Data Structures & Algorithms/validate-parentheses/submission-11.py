class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(',']':'[','}':'{'}
        for char in s:
            if stack and char in closeToOpen:
                if stack.pop() != closeToOpen[char]:
                    return False
            else:
                stack.append(char)
        return True if stack == [] else False