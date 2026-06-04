class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for char in s:
            if char in brackets:
                if len(stack) == 0 or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)

        return not stack
