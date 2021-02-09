def solution(s):
    num=len(s) ## 값의 초기화는 최초 문자열의 길이
    for i in range(1,(len(s)//2)+1):
        lst=[]
        start=0
        while start<=len(s)-1: ## 문자열을 단위별로 분리
            lst.append(s[start:start+i])
            start+=i
        start=0
        ans=''
        while start<len(lst): ## 압축과정
            count=1
            for nextNum in range(start+1,len(lst)+1):
                if nextNum!=len(lst) and lst[start]==lst[nextNum]: ## 문자가 같으면 갯수 증가
                    count+=1
                else:
                    if count!=1: ## 갯수가 1초과 일때에만 숫자표시
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

def solution3(s):## 순서가 우선 알파벳 관련 숫자 증가 시키고 그다음에 일치하지 않으면 중복 숫자 증가
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