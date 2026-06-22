class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]

        for ch in s:
            if ch =='(' or ch =='{' or ch == '[':
                stack.append(ch)
            elif stack and ((ch==')' and stack[-1] == '(') or (ch==']' and stack[-1] == '[') or (ch=='}' and stack[-1] == '{')):
                stack.pop()
            else:
                return False
        return len(stack)==0
        