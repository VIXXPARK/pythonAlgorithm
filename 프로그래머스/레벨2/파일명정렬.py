def solution(files):
    answer = []
    for idx,file in enumerate(files):
        val=[]
        mid=0
        end=0
        for i,v in enumerate(file):
            if v.isdigit():
                val.append(file[:i].lower())
                mid=i
                break
        end=mid
        flag=True
        while end<=len(file):
            if end==len(file) and file[end-1].isdigit():
                val.append(int(file[mid:end]))
                break
            elif len(file[mid:end])>5:
                val.append(int(file[mid:mid+5]))
                flag=False
                break
            elif end<len(file) and not file[end].isdigit():
                val.append(int(file[mid:end]))
                break
            end+=1
        x=file[end:] if flag else file[mid+5:]
        val.append(idx)
        val.append(x)
        val.append(file)
        answer.append(val)
    answer.sort()
    xx=[]
    for ans in answer:
        xx.append(ans[-1])
    return xx


################################################################################################################################
import re

def solution2(files):

    def key_function(fn):
        head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
        return [head,int(number)]

    return sorted(files, key = lambda x: key_function(x.lower()))

print(solution2(["dd1234124123ddd.zip",'img000012345', 'img1.png','img2','IMG02','F-15','foo010bar020.zip','B-50 Superfortress']))
