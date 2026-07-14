class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
        for c in word:
            current = current.children.setdefault(c, TrieNode())
        current.is_end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            current = trie.root

            for j in range(i, n):
                if s[j] not in current.children:
                    break

                current = current.children[s[j]]

                if current.is_end and dp[j + 1]:
                    dp[i] = True
                    break

        return dp[0]


# s = "catsincars"
# wordDict = ["cats","cat","sin","in","car"]

#      [c, a, t, s, i, n, c, a, r, s]
# dp = [F, F, F, F, F, F, F, F, F, F, T] (len(s) + 1)

#      [c, a, t, s, i, n, c, a, r, s]
# dp = [F, F, F, F, ?, F, F, F, F, F, T] (len(s) + 1)
#                   ^
#             dp[i] = dp[i + len(word)]


'''

"-----------------------------------------------------"

                            "neetcode"
            "neet"
                        "code"

"-----------------------------------------------------"

                        "applepenapple"
        "apple"
         "pen"
"apple"

"-----------------------------------------------------"

                                        "catsincars"
            "cats"              "cat"
             "in"               "sin"
            "car"               "car"
             "x"                 "x"

"-----------------------------------------------------"

'''