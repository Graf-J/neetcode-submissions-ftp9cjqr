class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        stack = []
        for token in tokens:
            if token not in operators.keys():
                stack.append(int(token))
            else:
                right_num, left_num = stack.pop(), stack.pop()
                result = operators[token](left_num, right_num)
                stack.append(result)

        return stack.pop()

