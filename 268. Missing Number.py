class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)+1):
            num ^= i
        for i in nums:
            num ^= i
        return num
