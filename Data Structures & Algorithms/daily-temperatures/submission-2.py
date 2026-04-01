class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack_desc = []
        for i, t in enumerate(temperatures):
            while stack_desc and t > stack_desc[-1][0]:
                _, pop_idx = stack_desc.pop()
                result[pop_idx] = i - pop_idx
            stack_desc.append((t, i))

        return result
