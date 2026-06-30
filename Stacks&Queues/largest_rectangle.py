class Solution(object):
    def prevsmall(self, arr):
        n = len(arr)
        st = []
        pse = [0] * n

        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            if st:
                pse[i] = st[-1]
            else:
                pse[i] = -1

            st.append(i)

        return pse

    def nextsmall(self, arr):
        n = len(arr)
        st = []
        nse = [0] * n

        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            if st:
                nse[i] = st[-1]
            else:
                nse[i] = -1

            st.append(i)

        return nse

    def largestRectangleArea(self, heights):
        n = len(heights)

        nse = self.nextsmall(heights)
        pse = self.prevsmall(heights)

        area = 0

        for i in range(n):
            height = heights[i]

            if nse[i] == -1:
                nse[i] = n

            width = nse[i] - pse[i] - 1
            curr_area = height * width

            area = max(area, curr_area)

        return area