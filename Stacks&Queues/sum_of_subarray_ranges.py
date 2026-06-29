class Solution(object):
    def sum_min(self,nums):
        n = len(nums)
        left =[0]*n
        right = [0]*n
        nse =[]
        for i in range(n-1,-1,-1):
            while nse and nums[nse[-1]]>=nums[i]:
                nse.pop()
            if nse:
                right[i] = nse[-1] -i
            else:
                right[i] = n-i
            nse.append(i)
        pse =[]
        for i in range(n):
            while pse and nums[pse[-1]] > nums[i]:
                 pse.pop()
            if pse:
                left[i] = i - pse[-1]
            else:
                left[i] = i+1
            pse.append(i)
        
        ans =0
        for i in range(n):
            ans = (ans + nums[i] * left[i] * right[i])
        return ans
    def sum_max(self,nums):
        n = len(nums)
        left =[0]*n
        right = [0]*n
        nge =[]
        for i in range(n-1,-1,-1):
            while nge and nums[nge[-1]]<=nums[i]:
                nge.pop()
            if nge:
                right[i] = nge[-1] -i
            else:
                right[i] = n-i
            nge.append(i)
        pge =[]
        for i in range(n):
            while pge and nums[pge[-1]] < nums[i]:
                pge.pop()
            if pge:
                left[i] = i - pge[-1]
            else:
                left[i] = i+1
            pge.append(i)
        
        ans =0
        for i in range(n):
            ans = (ans + nums[i] * left[i] * right[i])
        return ans

    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.sum_max(nums) - self.sum_min(nums)
        