class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Solution2 without division
        l = [1] * len(nums)

        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]

        r = 1
        for i in reversed(range(len(nums))):
            l[i] = l[i] * r
            r = r * nums[i]

        return l