def post_to_pre(exp):
    stack=[]
    for i in range(len(exp)):
        if (exp[i]>='A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z') or (exp[i]>='0' and exp[i]<='9'):
            stack.append(exp[i])
        else:
            t1 = stack[-1]
            stack.pop()
            t2 = stack[-1]
            stack.pop()
            ch = exp[i] + t2 + t1
            stack.append(ch)
    return stack[-1]

exp = "AB+C*"
print(post_to_pre(exp))