class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        arr[0]=nums[0]
        for i in range(0,len(nums)):
            arr[i]=arr[i-1]+nums[i]
        return arr
            
