class Solution:
    def countSubstrings(self, s: str) -> int:
        answer=0
        for start in range(len(s)):#  aba 꼴의 알파벳 확인(홀수 스타일)
            left=start-1
            right=start+1
            answer+=1
            if left<0 or right>=len(s):
                continue
            else:
                while left>=0 and right<len(s):
                    if s[left]==s[right]:
                        answer+=1
                        left-=1
                        right+=1
                    else:
                        break
        for start in range(len(s)-1): # abba 꼴의 알파벳 확인(짝수 스타일)
            partner=start+1
            if s[start]==s[partner]:
                answer+=1
                left=start-1
                right=partner+1
                while left>=0 and right<len(s):
                    if s[left]==s[right]:
                        answer+=1
                        left-=1
                        right+=1
                    else:
                        break
            else:
                continue
        return answer
                
            