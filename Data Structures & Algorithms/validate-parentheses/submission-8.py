class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in p_map:
                if len(stack) == 0:
                    return False
                c_pop = stack.pop()
                if p_map[c] != c_pop:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
