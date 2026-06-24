class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack =[]
        n = len(nums)
        nge=[-1]*n
       
        for i in range(2*n-1,-1,-1):
            while len(stack)!=0 and stack[-1] <= nums[i%n]:
                stack.pop()
            if i<n:
                if len(stack)==0:
                    nge[i]=-1
                else:
                    nge[i] = stack[-1]
            stack.append(nums[i%n])
        return nge
        