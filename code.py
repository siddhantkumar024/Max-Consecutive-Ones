class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxc=0
        c=0
        for num in nums:
            if num == 1:
                c+=1
                maxc=max(maxc,c)
            elif num==0:
                c=0
        return maxc
        
