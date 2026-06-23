def priority(exp):
    if exp=='**':
        return 3
    elif exp =='*' or exp=='/':
        return 2
    elif exp =='+' or exp =='-':
        return 1
    return -1 

def convert_to_postfix(exp):
    i=0
    stack =[]
    ans = ""
    for i in range(len(exp)):
        if (exp[i]>='A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z') or (exp[i]>='0' and exp[i]<='9'):
            ans +=exp[i]

        elif exp[i]=='(':
            stack.append(exp[i])

        elif exp[i]==')':
            while len(stack)!=0 and stack[-1]!='(':
                ch = stack.pop()
                ans +=ch
            stack.pop()
        
        else:
            while len(stack)!=0 and priority(exp[i]) <= priority(stack[-1]):
                ch = stack.pop()
                ans+=ch
            stack.append(exp[i])
    
    while len(stack)!=0:
        ch= stack.pop()
        ans+=ch
    return ans

exp = "A+B*(C-D)"
print(convert_to_postfix(exp))


        
