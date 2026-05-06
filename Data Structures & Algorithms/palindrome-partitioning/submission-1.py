class Solution:
    def is_palindrome(self, string):
        l, r = 0, len(string) - 1
        while l <= r:
            if string[l] != string[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []

        def dfs(offset: int, substrings: List[str]):
            if all(self.is_palindrome(substring) for substring in substrings):
                result.append(substrings.copy())
            if len(substrings) == 1 or len(substrings) == offset + 1:
                return

            for i in range(offset, len(substrings) - 1):
                first, second = substrings.pop(i), substrings.pop(i)
                first_len = len(first)
                substrings.insert(i, first + second)

                dfs(i, substrings)

                merged = substrings.pop(i)
                substrings.insert(i, merged[:first_len])
                substrings.insert(i + 1, merged[first_len:])

        dfs(0, list(s))
        return result