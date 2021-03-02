class Solution:
    def reconstructQueue(self, people):
        people = sorted(people,key=lambda x:(x[1],x[0]) )
        answer=[]
        while people:
            if not answer:
                answer.append(people.pop(0))
            else:
                x=people.pop(0)
                cnt=0
                loc=0
                for idx,v in enumerate(answer):
                    if cnt==x[1] and v[0]>=x[0]:
                        loc=idx
                        break
                    if v[0]>=x[0]:
                        cnt+=1
                if loc!=0:
                    answer.insert(loc,x)
                else:
                    answer.append(x)
        return answer

#################################################################
class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))        
        res = []        
        for p in people:
            if p[1] >= len(res):
                res.append(p)
            else:
                res.insert(p[1], p)
        return res