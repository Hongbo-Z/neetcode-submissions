class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        subString = ""

        digitsToChar = {
            '2':"abc",
            '3':"def",
            '4': "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, subString):
            if i == len(digits):
                res.append(subString)
                return
            for char in digitsToChar[digits[i]]:
                backtrack(i + 1, subString + char)
        
        if digits:
            backtrack(0, subString)
        return res