class Solution:
    def foreignDictionary(self, words):
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}
        for w_idx in range(len(words) - 1):
            w1, w2 = words[w_idx], words[w_idx + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]: # invalid case: "abc" before "ab"
                return ""

            j = 0
            while j < min_len and w1[j] == w2[j]:
                j += 1

            # only add an edge if we actually found a difference
            if j < min_len:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1

        q = deque(c for c, indeg in indegree.items() if indeg == 0)

        result = []
        while q:
            c = q.popleft()
            result.append(c)
            for out_c in adj[c]:
                indegree[out_c] -= 1
                if indegree[out_c] == 0:
                    q.append(out_c)

        return "".join(result) if len(result) == len(adj) else ""
