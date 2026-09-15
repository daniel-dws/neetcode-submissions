class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for idx, item in enumerate(nums):
            dict.setdefault(item, []).append(idx)

        for idx, cur_item in enumerate(nums):
            diff = target - cur_item
            if diff not in list(dict.keys()):
                continue
            if diff == cur_item:
                if len(dict[diff]) > 1:
                    return dict[diff][:2]
                else:
                    continue
            else:
                return [idx, dict[diff][0]]


            



        