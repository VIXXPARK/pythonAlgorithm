lst=[[6,1-1],[5,1-1],[4,1-1],[3,3-1],[2,3-1],[1,5-1]]
lst=sorted(lst,key=lambda x : (1/(x[1]+1),x[0]),reverse=True)
print(lst)