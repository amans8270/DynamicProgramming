class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count1=0
        count2=0
        prev = -float('inf')
        
        for i in nums:
            if(i<prev):
                count1+=1
            else:
                prev=i
        prev = float('inf')
        for i in reversed(nums):
            if(i>prev):
                count2+=1
            else:
                prev=i
        return min(count1 ,count2)<=1
                
