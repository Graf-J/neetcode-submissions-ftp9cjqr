class Solution:
    delimiter = "#"

    def encode(self, strs: List[str]) -> str:
        encoded_strings = []
        for string in strs:
            encoded_string = f"{len(string)}{self.delimiter}{string}"
            encoded_strings.append(encoded_string)

        return "".join(encoded_strings)

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            # Extract String Length
            j = i
            while s[j] != self.delimiter:
                j += 1
            len_string = int(s[i:j])

            # Extract String Value
            string = s[j + 1:j + 1 + len_string]
            strings.append(string)

            # Jump to next Word
            i = j + 1 + len_string

        return strings

        


            


