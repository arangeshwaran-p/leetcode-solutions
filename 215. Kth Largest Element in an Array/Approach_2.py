class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = sorted(nums)
        return n[-k]
        