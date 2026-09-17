class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        l = []
        zero_count = []
        for num in nums:
            if num != 0:
                product *= num
            elif num == 0:
                zero_count.append(0)
        
        for num in nums:
            if len(zero_count) == 0:
                l.append(product//num)
            elif len(zero_count) > 1:
                l.append(0)
            elif len(zero_count) == 1 and num ==0:
                l.append(product)
            else:
                l.append(0)
        return l

