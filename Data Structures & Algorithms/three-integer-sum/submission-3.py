class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        triplets = []
        for idx in range(len(nums)):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue

            l = idx + 1
            r = len(nums) - 1
            while l < r:
                triplet_sum = nums[idx] + nums[l] + nums[r]
                if triplet_sum < 0:
                    l += 1
                elif triplet_sum > 0:
                    r -= 1
                else:
                    triplets.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1

        return triplets