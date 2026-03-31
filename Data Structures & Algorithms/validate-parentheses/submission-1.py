class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        bracket_pair = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for current_bracket in s:
            if current_bracket in bracket_pair:
                stack.append(current_bracket)
            else:
                if not stack:
                    return False
                opening_bracket = stack.pop()
                closing_bracket = bracket_pair[opening_bracket]
                if current_bracket != closing_bracket:
                    return False

        if stack:
            return False

        return True