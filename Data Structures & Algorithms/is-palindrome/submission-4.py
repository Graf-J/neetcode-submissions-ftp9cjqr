class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not (
                ("A" <= s[l] <= "z") or 
                ("0" <= s[l] <= "9")
            ):
                l += 1
                continue
            if not (
                ("A" <= s[r] <= "z") or 
                ("0" <= s[r] <= "9")
            ):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True