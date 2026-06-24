def prefix_to_infix(exp):
    n = len(exp)
    stack=[]
    for i in range(n-1,-1,-1):
        if (exp[i]>='A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z') or (exp[i]>='0' and exp[i]<='9'):
            stack.append(exp[i])
        else:
            top1 = stack[-1]
            stack.pop()
            top2 = stack[-1]
            stack.pop()
            ch = '(' + top1 + exp[i] + top2 +')'
            stack.append(ch)
    return stack[-1]

exp = "*+AB-CD"
print(prefix_to_infix(exp))