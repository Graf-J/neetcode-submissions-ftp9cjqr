class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0
        hashset = set(nums)
        checked = set()
        for num in nums:
            if num in checked:
                continue
            
            checked.add(num)
            
            sequence = 1
            ctr = 1
            while True:
                if num - ctr not in hashset:
                    break

                sequence += 1
                checked.add(num - ctr)
                ctr += 1

            ctr = 1
            while True:
                if num + ctr not in hashset:
                    break

                sequence += 1
                checked.add(num + ctr)
                ctr += 1

            max_sequence = max(sequence, max_sequence)

        return max_sequence

            

        