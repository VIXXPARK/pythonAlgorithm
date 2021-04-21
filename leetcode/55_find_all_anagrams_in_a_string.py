class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        s=list(s);p=list(p)
        size=len(p)
        basket={};default={}
        answer=[]
        for i in range(size): ##기본 사전 형식으로 만들기
            if basket.get(s[i],0)==0:
                basket[s[i]]=1
            else:
                basket[s[i]]+=1

            if default.get(p[i],0)==0:
                default[p[i]]=1
            else:
                default[p[i]]+=1

        if(basket==default):
            answer.append(0)
        for i in range(1,len(s)-size+1):
            if basket[s[i-1]]==1:##해당 값이 1이면 삭제
                del basket[s[i-1]]
            elif basket[s[i-1]]>1:
                basket[s[i-1]]-=1

            if basket.get(s[i+size-1],0)==0:##추가된 값이 이미 존재하면 1추가, 없다면 1로 생성
                basket[s[i+size-1]]=1
            else:
                basket[s[i+size-1]]+=1

            if basket==default:##같으면 인덱스 추가
                answer.append(i)
        return answer

###############################################################


        