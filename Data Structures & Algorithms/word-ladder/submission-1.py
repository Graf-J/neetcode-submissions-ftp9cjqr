from collections import deque

class Solution:
    def diff_eq_1(self, w1: str, w2: str) -> bool:
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = {word: [] for word in wordList}
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.diff_eq_1(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])

        visited = set()

        q = deque()
        for word in wordList:
            if self.diff_eq_1(beginWord, word):
                q.append(word)
                visited.add(word)

        distance = 2
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return distance

                for neighbor in adj[word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

            distance += 1

        return 0