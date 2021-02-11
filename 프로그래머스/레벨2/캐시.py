def solution(cacheSize, cities):
    answer = 0
    cache=[]
    for i,val in enumerate(cities):
        cities[i]=cities[i].lower()
        try:
            if cache.index(cities[i])!=None:
                answer+=1
                del cache[cache.index(cities[i])]
                cache.append(cities[i])                
        except:
            if len(cache)+1<=cacheSize:
                    answer+=5
                    cache.append(cities[i])
            elif len(cache)!=0 and len(cache)==cacheSize:
                answer+=5
                cache.pop(0)
                cache.append(cities[i])
            else:
                answer+=5
    return answer
#################################################################
def solution2(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time