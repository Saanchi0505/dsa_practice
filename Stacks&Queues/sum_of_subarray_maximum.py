class Solution(object):
    def sumSubarrayMaxs(self, arr):
        mod = 10**9 +7
        n = len(arr)
        left = [0]*n
        right = [0]*n

        nge =[]
        for i in range(n-1,-1,-1):
            while nge and arr[nge[-1]] <= arr[i]:
                nge.pop()
            if nge:
                right[i] = nge[-1]-i
            else:
                right[i]= n-i
            nge.append(i)
        
        pge=[]
        for i in range(n):
            while pge and arr[pge[-1]]<arr[i]:
                pge.pop()
            if pge:
                left[i] = i- pge[-1]
            else:
                left[i] = i+1
            pge.append(i)
        ans = 0

        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % mod

        return ans
    
arr = [3, 1, 2, 4]
print(Solution().sumSubarrayMaxs(arr))