def partition(p):
    u,v='',''
    if p!='':
        stk=[]
        stk.append(p[0])
        init=p[0]
        for i in range(1,len(p)):
            if len(stk)!=0 and init!=p[i]:
                stk.pop()
                if i==len(p)-1:
                    u,v=p[:i+1],p[i+1:]
            elif len(stk)!=0 and init== p[i]:
                stk.append(p[i])
            else:
                u,v=p[:i],p[i:]
                break
    return u,v
def isRight(p):
    stk=[]
    for val in p:
        if val=='(': 
            stk.append('(')
        elif val==')' and len(stk)!=0 and stk.pop()=='(': 
            continue
        else: 
            return False
    return not stk       
def reverseParenthesis(p):
    ans=''
    for val in p:
        if val=='(': ans+=')'
        else: ans+='('
    return ans

def solution(p):
    answer = ''
    if p=='':
        return ''
    else:
        u,v=partition(p)
        if u!='':
            if isRight(u):
                return u+solution(v)
            else:
                return '('+solution(v)+')'+reverseParenthesis(u)[1:-1]

####################################################################################
def solution2(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))