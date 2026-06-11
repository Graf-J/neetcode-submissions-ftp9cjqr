class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = defaultdict(int)
        for task in tasks:
            task_freq[task] += 1
        task_freq = list(task_freq.values())
        heapq.heapify_max(task_freq)

        q, ctr = deque(), 0
        while task_freq or q:
            if q and q[0][1] == ctr:
                freq, _ = q.popleft()
                heapq.heappush_max(task_freq, freq)

            if task_freq:
                freq = heapq.heappop_max(task_freq)
                if freq > 1:
                    q.append((freq - 1, ctr + n + 1))

            ctr += 1

        return ctr


# Time-Complexity: O(N + N + N * log(N))
# Space-Complexity: O(26 + 26)

n = 2
task_freq = []
q = []
ctr = 5

