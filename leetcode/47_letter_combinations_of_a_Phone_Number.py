def letterCombinations(digits):
    dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
    cmb = [''] if digits else []
    for d in digits:
        cmb = [p + q for p in cmb for q in dict[d]]
    return cmb

print(letterCombinations("23"))

######################################################################
class Solution: ## 내 풀이
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        
        board={}
        board["2"]=["a","b","c"];board["3"]=["d","e","f"];board["4"]=["g","h","i"];board["5"]=["j","k","l"]
        board["6"]=["m","n","o"];board["7"]=["p","q","r","s"];board["8"]=["t","u","v"];board["9"]=["w","x","y","z"]
        digits=list(digits)
        answer=[]
        def mNn(start,finish,ans):
            if start==finish:
                answer.append(''.join(ans[:]))
                return
            
            for val in board[digits[start]]:
                ans.append(val)
                mNn(start+1,finish,ans)
                ans.pop()
        
        mNn(0,len(digits),[])
        return answer
                