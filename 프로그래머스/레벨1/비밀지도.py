def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        str=''
        a1=list(format(arr1[i],'b').zfill(n)) ## 일반적으로 이진법으로 바꿀때는 bin이라고 작성하지만, format을 통하여 작성할때에는 format(num,'b')이라 한다.
        a2=list(format(arr2[i],'b').zfill(n)) ## zfill은 정해진 숫자에서 남는 부분을 0을 채워주는 메소드이다. 
        for j in range(n):                    ## 그 외에도 rjust는 오른쪽으로 정렬하고 남는 자리는 정해준 숫자를 채워준다. num = "11".rjust(5,"0") => "00011"
            if int(a1[j])+int(a2[j])!=0:str+='#'# ljust는 이름보면 알 수 있듯이 왼쪽 정렬하고 남는 자리는 정해준 숫자를 채워준다. num= "11".ljust(5,"0") =>"11000"
            else:str+=' '
        answer.append(str)
    return answer
####################################
# method에 관하여 아무것도 모를 때 
def binary(num):
    ans=[]
    while num!=0:
        ans.append(num%2)
        num=num//2
    return ans
def solution2(n, arr1, arr2):
    answer = []
    for i in range(n):
        up=binary(arr1[i])
        down=binary(arr2[i])
        while len(up)<n:
            up.append(0)
        while len(down)<n:
            down.append(0)
        up.reverse()
        down.reverse()
        val=''
        for j in range(n):
            if up[j]+down[j]!=0:
                val+='#'  
            else:
                val+=' '
        answer.append(val)
    return answer
