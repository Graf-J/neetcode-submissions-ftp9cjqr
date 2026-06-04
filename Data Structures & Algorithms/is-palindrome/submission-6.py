class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not ("A" <= s[l] <= "z" or "0" <= s[l] <= "9") and l < len(s) - 1:
                l += 1
            while not ("A" <= s[r] <= "z" or "0" <= s[r] <= "9") and r > 0:
                r -= 1

            if l >= r:
                break

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True
