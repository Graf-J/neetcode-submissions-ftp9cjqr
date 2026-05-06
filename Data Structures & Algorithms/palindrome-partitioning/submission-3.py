class Solution:
    def is_palindrome(self, string):
        l, r = 0, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        def dfs(start: int, path: List[str]):
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if self.is_palindrome(substring):
                    path.append(substring)
                    dfs(end, path)
                    path.pop()

        dfs(0, [])
        return result

