def pre_to_post(exp):
    n = len(exp)
    stack =[]
    for i in range(n-1,-1,-1):
        if (exp[i]>='A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z') or (exp[i]>='0' and exp[i]<='9'):
            stack.append(exp[i])
        else:
            t1 = stack[-1]
            stack.pop()
            t2 = stack[-1]
            stack.pop()
            ch = t1 + t2 + exp[i]
            stack.append(ch)
    return stack[-1]

exp = "*+ABC"
print(pre_to_post(exp))