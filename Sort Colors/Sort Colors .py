class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red=0
        white=0
        for i in nums:
            if i==0:
                red+=1
            elif i==1:
                white +=1
        for i in range(len(nums)):
            if red !=0:
                nums[i]=0
                red-=1
            elif white !=0:
                nums[i]=1
                white -=1
            else:
                nums[i]=2 
        
