def post_to_in(exp):
    stack = []
    i=0
    for i in range(len(exp)):
        if (exp[i] >='A' and exp[i]<='Z') or (exp[i]>='a' and exp[i]<='z') or (exp[i]>='0' and exp[i]<='9'):
            stack.append(exp[i])
        else:
            t1 = stack[-1]
            stack.pop()
            t2 = stack[-1]
            stack.pop()
            ch = '(' + t2  + exp[i] + t1 + ')'
            stack.append(ch)
    return stack[-1]

exp = "ABC/-AK/L-*"
print(post_to_in(exp))