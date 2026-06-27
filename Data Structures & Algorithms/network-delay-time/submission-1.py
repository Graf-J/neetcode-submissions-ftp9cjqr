class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {node: [] for node in range(1, n + 1)}
        for u, v, t in times:
            adj[u].append((v, t))

        node_time_map = {}
        def dfs(node: int, time: int):
            if node_time_map.get(node, float("inf")) <= time:
                return

            node_time_map[node] = time
            for neighbor, weight in adj[node]:
                dfs(neighbor, time + weight)

        dfs(k, 0)
        max_time = max(node_time_map.values())
        return max_time if len(node_time_map) == n else -1


