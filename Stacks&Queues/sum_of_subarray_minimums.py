class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10**9 +7
        n =  len(arr)
        left = [0]*n
        right = [0]*n

        pse=[]
        for i in range(n):
            while pse and arr[pse[-1]] > arr[i]:
                pse.pop()
            
            if not pse:
                left[i] = i+1
            else:
                left[i] = i - pse[-1]
            pse.append(i)
        nse =[]
        for i in range(n-1,-1,-1):
            while nse and arr[nse[-1]] >= arr[i]:
                nse.pop()
            if not nse:
                right[i] = n-i
            else:
                right[i] = nse[-1]-i
            nse.append(i)
        
        ans=0
        for i in range(n):
            ans = (ans+ arr[i]  *left[i]*right[i])%mod
        return ans