class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft, maxLeft = 0, 0
        for char in s:
            if char == "(":
                minLeft, maxLeft = minLeft + 1, maxLeft + 1
            elif char == ")":
                minLeft, maxLeft = minLeft - 1, maxLeft - 1
            else:
                minLeft, maxLeft = minLeft - 1, maxLeft + 1
            if maxLeft < 0:
                return False
            if minLeft < 0: # minLeft < 0 is not a real state, as we can never have negative number of unmatched left parantheses, once it goes below zero, we must clamp it.
                minLeft = 0
        return minLeft == 0