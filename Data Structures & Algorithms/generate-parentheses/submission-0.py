class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(parentheses: str, opening: int, closing: int, result: List[str] = []):
            if len(parentheses) == 2 * n:
                result.append(parentheses)
                return

            if opening < n:
                rec(parentheses + '(', opening + 1, closing, result)
            if opening > closing:
                rec(parentheses + ')', opening, closing + 1, result)

            return result
        
        return rec('(', 1, 0)