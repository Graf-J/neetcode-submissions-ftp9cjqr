class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = set()
        def dfs(s_idx):
            if s_idx == len(s):
                return True
            if s_idx in memo:
                return False

            tmp = s_idx
            for word in wordDict:
                w_idx, s_idx = 0, tmp
                while w_idx < len(word) and s_idx < len(s) and word[w_idx] == s[s_idx]:
                    w_idx, s_idx = w_idx + 1, s_idx + 1
                
                if w_idx != len(word):
                    continue

                if dfs(s_idx):
                    return True

            memo.add(s_idx)
            return False

        return dfs(0)



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