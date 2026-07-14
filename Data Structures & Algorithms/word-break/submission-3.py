class TrieNode:
    def __init__(self):
        self.chars = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.chars.setdefault(char, TrieNode())
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.chars:
                return False
            current = current.chars[char]
        return current.is_end


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s) + 1)
        dp[-1] = True
        found_idxs = [len(s) + 1]
        for i in range(len(s) - 1, -1, -1):
            for found_idx in found_idxs:
                if not trie.search(s[i:found_idx]):
                    continue

                dp[i] = True
                found_idxs.append(i)
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