class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0]*(length)
        right = [0]*(length)
        res = [0]*(length)
        left[0]=right[length-1]=1
        for i in range(1,length):
            left[i] = left[i-1] * nums[i - 1]
        for i in range(length-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(length):
            res[i]=left[i]*right[i]
        return res
        

