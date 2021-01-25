def solution1(new_id):
    new_id=new_id.lower()
    stk=''
    for alpha in new_id:
        if alpha.isalpha() or alpha.isdigit() or alpha=='-' or alpha=='_' or alpha=='.':
            if len(stk)!=0:
                if stk[-1]=='.' and alpha=='.':
                    pass
                else:
                    stk+=alpha
            else:
                stk+=alpha
    stk=list(stk)
    if len(stk)!=0 and stk[0]=='.':
        del stk[0]
    if len(stk)!=0 and stk[-1]=='.':
        del stk[-1]
    if len(stk)==0:
        stk+='a'
    if len(stk)>=16:
        stk=stk[0:15]
        if stk[-1]=='.':
            stk.pop()
    if len(stk)<=2:
        word=stk[-1]
        while len(stk)<3:
            stk+=word     
    return ''.join(stk)
print(solution1('abcdefghijklmn.p'))

##################
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st