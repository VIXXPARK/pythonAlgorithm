# insert(입력할 index, value)
a=[1,2,3]
a.insert(1,5)
# print(a) [1,5,2,3]

# +로 더하기
x=[1,2,3]
y=[4,5,6]
z=x+y
# print(z) [1,2,3,4,5,6]

# extend 메소드
k=[1,2,3]
k.extend([4,5,6])
# k -> [1,2,3,4,5,6]

# del index를 통한 삭제
g= [1,2,3,4,5,6,7]
del g[1] # 해당 인덱스 없을 경우 error를 띄운다
# print(g) [1,3,4,5,6,7]

# remove value를 통한 삭제
g = [1,2,3,4,5,6,7]
g.remove(2)
# print(g) [1,3,4,5,6,7]


# index 메소드
g=[7,6,5,4,3,2,1]
# print(g.index(2)) list.index(값) 값에 대한 해당 자리를 리턴한다.

#count
cnt = [1,1,5,6,7,8,8,9]
# print(cnt.count(8)) 괄호 안에 있는 해당 갯수를 리턴한다.

a= [1,2,3]
b=a # 얕은 복사
b[0]=5
a # [5,2,3]

# 하지만 str 문자열에서 얕은 복사를 해도 값을 변경 했을 때 같이 변하지는 않는다
a = "abc"
b=a
# print(a) abc
# print(b) abc
b="abcd"
# print(a) abc
# print(b) abcd

a = [1,2,3]
b = a[:]
# print(id(a))  2206184342216
# print(id(b))  2206180239688
# print(a==b)  True
# print(a is b)  False
# b[0]=5
# print(a) [1, 2, 3]
# print(b) [5, 2, 3] 서로 값에 영향을 주지 않는다.

# 하지만 이러한 슬라이싱 또한 얕은 복사에 해당한다.

a= [[1,2],[3,4]]
b=a[:]
# print(id(a)) 2670547010440
# print(id(b)) 2670547010312
# id(a) 와 id(b) id는 같은 것에 비하여
# print(id(a[0])) 2670546993544
# print(id(b[0])) 2670546993544
# id(a[0]) 와 id(b[0]) 의 id는 다르다.

# a[0]= [8,9]
# print(a) [[8, 9], [3, 4]] 
# print(b) [[1, 2], [3, 4]]
# 재할당하는 경우에는 문제가 없습니다.

# a[0][0]=3
# print(a) [[3, 2], [3, 4]]
# print(b) [[3, 2], [3, 4]]
# 하지만 값을 바꾸면 id가 같기에 같이 변한다.

# a[1].append(5)
# print(a) [[1, 2], [3, 4, 5]]
# print(b) [[1, 2], [3, 4, 5]]
# 추가 또한 같다.

# 완전히 새로운 객체를 원한다면 deepcopy를 사용해야 한다.
import copy
b=copy.deepcopy(a)
a[1].append(5)
# print(a) [[1, 2], [3, 4, 5]]
# print(b) [[1, 2], [3, 4]]
