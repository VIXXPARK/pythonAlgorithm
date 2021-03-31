class Solution:
    def decodeString(self, s: str) -> str:
        num=[]
        left=[]
        val=[]
        ans=''
        tmp=[]
        numtmp=[]
        for c in s:
            if c.isdigit():
                numtmp.append(c)
            elif not left and c not in ['[',']']:
                ans+=c
            elif c=='[':
                if tmp:
                    val.append(''.join(tmp[:]))
                    tmp=[]
                key=len(val)
                left.append(key)
                num.append(int(''.join(numtmp)))
                numtmp=[]
                
            elif 'a'<=c<='z':
                tmp.append(c)
            elif c==']':
                if tmp:
                    left.pop()
                    x=''.join(tmp)*num.pop()
                    tmp=[]
                    if left:
                        val.append(x)
                    else:
                        ans+=x
                else:
                    dot=left.pop()
                    
                    
                    if left:
                        val=val[:dot]
                        val.append(x)
                    else:
                        x=''.join(val)*num.pop()
                        val=[]
                        ans+=x
        return ans

s=Solution()
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))