class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_list = []
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in nums:
                pos = nums.index(difference)
                if pos != idx:
                    indices_list.append(idx)
                    indices_list.append(pos)
        # return indices_list
        return list(set(indices_list))



        