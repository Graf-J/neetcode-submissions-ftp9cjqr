class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1, nums[0]]
        for idx in range(1, len(nums) - 1):
            prefix.append(prefix[idx] * nums[idx])

        postfix = [1, nums[-1]]
        for idx in range(1, len(nums) - 1):
            postfix.append(postfix[idx] * nums[-idx - 1])

        products = []
        for idx in range(len(nums)):
            products.append(prefix[idx] * postfix[-idx - 1])

        return products

        
        
            