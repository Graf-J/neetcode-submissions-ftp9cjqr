class Solution:
    def isPalindrome(self, s: str) -> bool:
        cursor_left_idx = 0
        cursor_right_idx = len(s) - 1

        while cursor_left_idx < cursor_right_idx:
            if not s[cursor_left_idx].isalnum():
                cursor_left_idx += 1
                continue
            if not s[cursor_right_idx].isalnum():
                cursor_right_idx -= 1
                continue

            if s[cursor_left_idx].lower() != s[cursor_right_idx].lower():
                return False

            cursor_left_idx += 1
            cursor_right_idx -= 1

        return True
            