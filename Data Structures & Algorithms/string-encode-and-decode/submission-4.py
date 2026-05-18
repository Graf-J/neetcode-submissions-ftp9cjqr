class Solution:
    delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []
        for s in strs:
            encoded_strs.append(str(len(s)) + self.delimiter + s)
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        l = 0
        while l < len(s):
            # Extract Length of String
            r = l + 1
            while s[r] != self.delimiter:
                r += 1
            s_len = int(s[l:r])

            # Extract String
            l, r = r + 1, r + 1 + s_len
            decoded_strs.append(s[l:r])
            l = r

        return decoded_strs


# # (1)
# []
# Encoded: ""
# Decoded: []

# # (2)
# [Hello, World]
# Encoded: "5#Hello5#World"
# Decoded: []

# # (4)
# [H, 5]
# Encoded: "1#H1#5"

# # (3)
# [Hello4, WorldWorld]
