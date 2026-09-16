class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx, num in enumerate(nums):
            if idx+1 != len(nums) and num == nums[idx+1]:
                return True
        return False