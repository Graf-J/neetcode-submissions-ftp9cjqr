class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        prev_anchor = None
        for anchor in range(len(nums) - 2):
            # Skip same Value to avoid Duplicates
            if nums[anchor] == prev_anchor:
                continue
            prev_anchor = nums[anchor]

            l = anchor + 1
            r = len(nums) - 1
            while l < r:
                a_val, l_val, r_val = nums[anchor], nums[l], nums[r]
                s = a_val + l_val + r_val
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append([a_val, l_val, r_val])
                    # Skip same Value to avoid Duplicates
                    while nums[l] == l_val and l < len(nums) - 1:
                        l += 1
                    while nums[r] == r_val and r > 0:
                        r -= 1

        return result


 # O(N * log(N) + N^2)







