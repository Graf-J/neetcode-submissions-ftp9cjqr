class Solution:
    def can_decode(self, num: str) -> bool:
        assert len(num) <= 2
        if len(num) == 1:
            return num != "0"
        else:
            if num[0] == "0":
                return False
            return 10 <= int(num) <= 26

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0 if s == "0" else 1

        # Initialize
        dp = [0] * n
        dp[-1] = int(self.can_decode(s[-1]))
        dp[-2] = int(self.can_decode(s[-2]) and dp[-1]) + int(self.can_decode(s[-2:]))

        # Run DP-Algorithm
        for i in range(len(s) - 3, -1, -1):
            single = double = 0
            if self.can_decode(s[i]):
                single = dp[i + 1]
            if self.can_decode(s[i:i+2]):
                double = dp[i + 2]
            dp[i] = single + double

        return dp[0]
        



'''

"1120724"

                    O
        1                      11
    1       12             2        20
 2    20  2                      7
    7                          2  (24)
  2  (24)                   (4)
(4)      


single = 0
double = 0
if can_decode(single):
    single = dp[i + 1]
if can_decode(double):
    double = dp[i + 2]
dp[i] = single + double

"1  1  2  0  7  2  4"
[?, ?, ?, ?, ?, 2, 1]
             ^
7 works, 72 fails
-> keep 2

"1  1  2  0  7  2  4"
[?, ?, ?, ?, 2, 2, 1]
          ^
0 fails, 07 fails
-> set 0

"1  1  2  0  7  2  4"
[?, ?, ?, 0, 2, 2, 1]
       ^
2 works, 20 works
-> set 0 + 2 = 2

"1  1  2  0  7  2  4"
[?, ?, 2, 0, 2, 2, 1]
    ^
1 works, 12 works
-> set 2 + 0 = 2

"1  1  2  0  7  2  4"
[?, 2, 2, 0, 2, 2, 1]
1 works, 11 works
-> set 2 + 2 = 4

[(4), 2, 2, 0, 2, 2, 1]

'''