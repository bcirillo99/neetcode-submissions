class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*(length)
        left_prod = 1
        for i in range(length):
            res[i]= left_prod
            left_prod*=nums[i]
        right_prod = 1
        for i in range(length-1,-1,-1):
            res[i]*=right_prod
            right_prod*=nums[i]
        return res
        

