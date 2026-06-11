class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        num_chars = {
                        "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []
        def dfs(path, i):
            if i == len(digits):
                result.append("".join(path))
                return
            
            for char in num_chars[digits[i]]:
                path.append(char)
                dfs(path, i + 1)
                path.pop()

        dfs([], 0)
        return result