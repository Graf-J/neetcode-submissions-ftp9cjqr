class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        triplets = set()
        for idx in range(len(nums) - 2):
            l = idx + 1
            r = len(nums) - 1

            while l < r:
                if nums[idx] + nums[l] + nums[r] == 0:
                    triplets.add((nums[idx], nums[l], nums[r]))
                    l += 1
                elif nums[idx] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return [list(triplet) for triplet in triplets]
