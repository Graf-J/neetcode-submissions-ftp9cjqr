class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        for idx, temperature in enumerate(temperatures):
            while monotonic_stack and monotonic_stack[-1][0] < temperature:
                _, temp_idx = monotonic_stack.pop()
                temperatures[temp_idx] = idx - temp_idx
            monotonic_stack.append((temperature, idx))

        for _, temp_idx in monotonic_stack:
            temperatures[temp_idx] = 0

        return temperatures