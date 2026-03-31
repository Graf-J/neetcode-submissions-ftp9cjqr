class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
                continue
            if token == '-':
                stack.append(-stack.pop() + stack.pop())
                continue
            if token == '*':
                stack.append(stack.pop() * stack.pop())
                continue
            if token == '/':
                stack.append(math.trunc((1 / stack.pop()) * stack.pop()))
                continue

            stack.append(int(token))

        return stack.pop()

            