class MinStack(object):

    def __init__(self):
        self.st =[]
        self.mini =None

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if len(self.st)==0:
            self.st.append(value)
            self.mini=value
        else:
            if value>=self.mini :
                self.st.append(value)
            else:
                self.st.append(2*value-self.mini)
                self.mini = value
    def pop(self):
        """
        :rtype: None
        """
        if len(self.st)==0:
            return
        x = self.st[-1]
        self.st.pop()
        if x<self.mini:
            self.mini = 2*self.mini -x

    def top(self):
        """
        :rtype: int
        """
        x = self.st[-1]
        if x<self.mini:
            return self.mini
        else:
            return x
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()