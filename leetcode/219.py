class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if len(window) > k:
                window.remove(nums[i - k - 1])
            if num in window:
                return True
            window.add(num)
        return False
