def solution1(new_id):
    new_id=list(new_id.lower())
    lst=[]
    for i,x in enumerate(new_id):
        if x in ['-','_','.'] or x.isdigit() or x.isalpha():
            if len(lst)!=0 and lst[-1]=='.' and x=='.':
                continue
            elif len(lst)==0 and x=='.':
                continue
            lst.append(x)
    if len(lst)!=0 and lst[-1]=='.': lst.pop()
    if len(lst)==0:
        lst.append('a')
    if len(lst)>=16:
        lst=lst[:15]
        if lst[-1]=='.':
            lst.pop()
    if len(lst)<=2:
        addChar=lst[-1]
        while len(lst)<3:
            lst.append(addChar)
    return ''.join(lst)
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