class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                top_t, top_idx = stack.pop()
                result[top_idx] = idx - top_idx

            stack.append((t, idx))

        return result


# Time: O(N)
# Space: O(N)
