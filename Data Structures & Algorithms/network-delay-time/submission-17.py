class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))

        distance = [float("inf")] * n
        distance[k - 1] = 0
        heap = [(0, k - 1)]

        while heap:
            dist, node = heapq.heappop(heap)
            if dist != distance[node]:
                continue
            
            for neighbour, weight in adj[node]:
                if dist + weight < distance[neighbour]:
                    distance[neighbour] = dist + weight
                    heapq.heappush(heap, (dist + weight, neighbour))

        max_dist = max(distance)
        return -1 if max_dist == float("inf") else max_dist


















































        # adj = defaultdict(list)
        # for u, v, t in times:
        #     adj[u].append((v, t))

        # distances = defaultdict(lambda: float("inf"))
        # distances[k] = 0

        # heap = [(0, k)]

        # num_nodes_visited = 0
        # max_distance = 0
        # while heap:
        #     dist, node = heapq.heappop(heap)
        #     if distances[node] != dist:
        #         continue
        #     max_distance = max(max_distance, dist)
        #     num_nodes_visited += 1

        #     for neighbour, weight in adj[node]:
        #         if dist + weight < distances[neighbour]:
        #             distances[neighbour] = dist + weight
        #             heapq.heappush(heap, (dist + weight, neighbour))

        # return max_distance if num_nodes_visited == n else -1

