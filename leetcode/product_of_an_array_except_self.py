class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1]*n
        left_product = 1
        right_product = 1
        for i in range(n):
            result[i]*=left_product
            left_product*=nums[i]
            result[n-i-1]*=right_product
            right_product*=nums[n-i-1]
        return result