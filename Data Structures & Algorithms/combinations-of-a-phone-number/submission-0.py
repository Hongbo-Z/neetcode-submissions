class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        subStr = ""
        digitTochar = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(i, subStr):
            if len(subStr) == len(digits):
                res.append(subStr)
                return
            for char in digitTochar[digits[i]]:
                backtrack(i+1, subStr + char)
        
        if digits:
            backtrack(0, subStr)
            return res
        else:
            return []
        
    
