class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
        ]

        result = []
        def dfs(i: int, path: List[str]):
            if i == len(digits):
                result.append("".join(path))
                return

            digit = int(digits[i])
            for letter in letters[digit - 2]:
                path.append(letter)
                dfs(i + 1, path)
                path.pop()

        if digits:
            dfs(0, [])
            
        return result








