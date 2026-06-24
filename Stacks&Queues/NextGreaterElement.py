class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nge ={}
        stack =[]
        n = len(nums2)
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                nge[nums2[i]] = stack[-1]
            else:
                nge[nums2[i]] = -1
            stack.append(nums2[i])
        ans =[]

        for num in nums1:
            ans.append(nge[num])
        return ans
        