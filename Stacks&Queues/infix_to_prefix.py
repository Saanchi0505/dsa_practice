def priority(exp):
    if exp =='**':
        return 3
    elif exp =='*' or exp == '/':
        return 2
    elif exp =='+' or exp == '-':
        return 1
    return -1

def infix_to_post(exp):
    i=0
    stack  =[]
    ans = ""
    for i in range(len(exp)):
        if (exp[i] >= 'A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z') or (exp[i]>='0' and exp[i]<='1'):
            ans += exp[i]
        
        elif exp[i]=='(':
            stack.append(exp[i])
        
        elif exp[i] == ')':
            while len(stack)!=0 and stack[-1]!='(':
                ch = stack.pop()
                ans+=ch
            stack.pop()
        
        else:
            if exp[i] == '**':
                while len(stack)!=0 and priority(exp[i])<=priority(stack[-1]):
                    ch = stack.pop()
                    ans+=ch
            else:
                while len(stack)!=0 and priority(exp[i]) < priority(stack[-1]):
                    ch = stack.pop()
                    ans+=ch
            stack.append(exp[i])
    
    while len(stack)!=0:
        ch  = stack.pop()
        ans+=ch
    return ans

def infix_to_prefix(exp):
    exp = exp[::-1]
    temp= ""
    for ch in exp:
        if ch =='(':
            temp+=')'
        elif ch == ')':
            temp +='('
        else:
            temp+=ch
    
    postfix  = infix_to_post(temp)
    prefix = postfix[::-1]
    return prefix

exp = "(A-B/C)*(A/K-L)"
print(infix_to_prefix(exp))
