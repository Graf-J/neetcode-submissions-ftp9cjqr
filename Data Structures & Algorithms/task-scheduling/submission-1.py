class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_freq = defaultdict(int)
        for task in tasks:
            char_freq[task] += 1
        task_freq_heap = list(char_freq.values())
        heapq.heapify_max(task_freq_heap)

        ctr = 0
        q = deque([])
        while task_freq_heap or q:
            if q:
                if ctr - q[-1][1] > n:
                    q_task_freq, q_task_insert = q.pop()
                    heapq.heappush_max(task_freq_heap, q_task_freq)

            if task_freq_heap:
                task_freq = heapq.heappop_max(task_freq_heap)
                if task_freq > 1:
                    q.appendleft((task_freq - 1, ctr))
            ctr += 1

        return ctr


# n = 3
# task_freq_heap = [1]
# ctr = 5
# q = [(1, 4), (0, 2)]

