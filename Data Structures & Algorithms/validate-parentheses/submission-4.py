class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if len(stack) == 0 or stack.pop() != brackets[bracket]:
                    return False

        return len(stack) == 0