class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st =[]
        for i  in range(len(asteroids)):
            if asteroids[i] >0:
                st.append(asteroids[i])
            else:
                while st and st[-1]>0 and st[-1]<abs(asteroids[i]):
                    st.pop()
                if st and st[-1]==abs(asteroids[i]):
                    st.pop()
                elif len(st)==0 or st[-1] <0:
                    st.append(asteroids[i])
        return st