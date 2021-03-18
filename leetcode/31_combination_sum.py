class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer=[]
        def nNm(cand,ans,answer,total,cur):
            if total>=target:
                if total==target:
                    answer.append(ans[:])
                return
            for idx in range(cur,len(cand)):
                if total+cand[idx]<=target:
                    ans.append(cand[idx])
                    total+=cand[idx]
                    nNm(cand,ans,answer,total,idx)
                    total-=cand[idx]
                    ans.pop()
        nNm(candidates,[],answer,0,0)
        return answer