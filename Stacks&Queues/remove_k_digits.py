class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st=[]
        n  = len(num)
        for i in range(n):
            while st and k>0 and st[-1] > num[i]:
                st.pop()
                k-=1
            st.append(num[i])
        while k>0:
            st.pop()
            k-=1
        if not st:
            return '0'
        res = "".join(st).lstrip('0')
        return res if res else "0"