class Solution:
	# @param A : list of integers
	# @return a list of integers
    def prevSmaller(self, A):
        n= len(A)
        prevSmallerlist =[-1]*n
        stack=[]
        
        for i in range(n):
            while len(stack)!=0 and stack[-1]>=A[i]:
                stack.pop()
            if len(stack)==0:
                prevSmallerlist[i] = -1
            else:
                prevSmallerlist[i] = stack[-1]
            stack.append(A[i])
        return prevSmallerlist