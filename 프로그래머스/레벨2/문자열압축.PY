import sys
def solution(s):
    if len(s)==1:
        return 1
    num=sys.maxsize
    for i in range(1,len(s)):
        lst=[]
        start=0
        while start<=len(s)-1:
            lst.append(s[start:start+i])
            start+=i
        start=0
        ans=''
        while start<len(lst):
            count=1
            for nextNum in range(start+1,len(lst)+1):
                
                if nextNum==len(lst):
                    if count!=1:
                        ch=str(count)+lst[start]
                        ans+=ch
                        count=1
                        start+=1
                    else:
                        ans+=lst[start]
                        start+=1
                    break
                elif lst[start]==lst[nextNum]:
                    count+=1
                else:
                    if count!=1:
                        ch=str(count)+lst[start]
                        ans+=ch
                        count=1
                        start+=1
                    else:
                        ans+=lst[start]
                        start+=1
                    break
                    
                start+=1
        num=min(num,len(ans))
    return num

#############################################################
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution2(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
##############################################################################################################

def solution3(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1):
        d = 0
        comp = ''
        c = 1
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            if comp == temp:
                c += 1
            elif comp != temp:
                d += len(temp)
                if c > 1:
                    d += len("{}".format(c))
                c = 1
                comp = temp
        if c > 1:
            d += len("{}".format(c))
        answer = min(answer, d)
    return answer