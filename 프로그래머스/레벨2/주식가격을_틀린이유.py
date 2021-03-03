import time
# answer=[]
start = time.time()

# for i in range(int(10e4)):
#     answer.insert(0,i)


answer = [0 for _ in range(10000)]
for i in range(10000):
    for j in range(100):
        answer[i]+=1
    
finish = time.time()-start
print(finish)

# 주식가격을 틀린 이유는 다음 위와 같다. 
# insert 였을 때 2.2891643047332764
# 미리 리스트로 만들었을 때  0.08078384399414062
