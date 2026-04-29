class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        task_freq = list(task_counter.values())
        heapq.heapify_max(task_freq)

        cycle, q = 0, deque()
        while task_freq or q:
            if q and q[-1][1] == cycle:
                heapq.heappush_max(task_freq, q.pop()[0])

            if task_freq:
                freq = heapq.heappop_max(task_freq)
                if freq > 1:
                    q.appendleft((freq - 1, cycle + n + 1))

            cycle += 1

        return cycle