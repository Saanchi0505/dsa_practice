class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans =0
        lmax=0
        rmax=0
        l=0
        n = len(height)
        r=n-1
        while l<r:
            lmax = max(lmax,height[l])
            rmax = max(rmax,height[r])
            if lmax<rmax:
                ans+= lmax - height[l]
                l+=1
            else:
                ans+=rmax-height[r]
                r-=1
        return ans
        