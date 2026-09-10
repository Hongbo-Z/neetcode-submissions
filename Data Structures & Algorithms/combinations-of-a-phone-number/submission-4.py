class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        substring = ""

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

        def dfs(i, substring):
            if i == len(digits):
                res.append(substring)
                return
            
            for chr in digitsToChar[digits[i]]:
                dfs(i + 1, substring + chr)
        if digits:
            dfs(0, substring)
        return res
                