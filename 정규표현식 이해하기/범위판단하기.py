import re
# [ ](대괄호) 안에 숫자 범위를 넣으며 * 또는 +를 붙입니다. 숫자 범위는 0-9처럼 표현하며 *는 문자(숫자)가 0개 이상 있는지, +는 1개 이상 있는지 판단합니다

print(re.match('[0-9]*','1234')) #1234는 0부터 9까지 숫자가 0개 이상 있으므로 패턴이 매칭됨
#<re.Match object; span=(0, 4), match='1234'>
print(re.match('[0-9]+','1234')) #1234는 0부터 9까지 숫자가 1개 이상 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 4), match='1234'>
print(re.match('[0-9]+','abcd')) #abcd는 0부터 9까지 숫자가 1개 이상 없으므로 패턴에 매칭되지 않음
#None

print(re.match('a*b','b')) #b에는 a가 0개 이상 있으므로 패턴에 매칭됨
# re.Match object; span=(0, 1), match='b'>
print(re.match('a+b','b')) #b에는 a가 1개 이상 없으므로 패턴에 매칭되지 않음
#None
print(re.match('a*b','aab')) #aab에는 a가 0개 이상 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 3), match='aab'>
print(re.match('a+b','aab')) #aab에는 a가 1개 이상 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 3), match='aab'>


# 문자가 한 개만 있는지 판단할 때는 어떻게 해야 할까요? 이때는 ?와 .을 사용합니다. 
# ?는 ? 앞의 문자(범위)가 0개 또는 1개인지 판단하고, .은 .이 있는 위치에 아무 문자(숫자)가 1개 있는지 판단합니다

print(re.match('abc?d','abd')) #abd에서 c위치에 c가 0개 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 3), match='abd'>
print(re.match('ab[0-9]?c','ab3c')) # [0-9] 위치에 숫자가 1개 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 4), match='ab3c'>
print(re.match('ab.d','abxd')) # .이 있는 위치에 문자가 1개 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 4), match='abxd'>
print(re.match('ab.d','ab##d')) # .이 있는 위치에 문자가 2개 이상이므로 None 발생
#None

# 그럼 문자(숫자)가 정확히 몇 개 있는지 판단하고 싶을 수도 있겠죠? 이때는 문자 뒤에 {개수} 형식을 지정합니다. 
# 문자열의 경우에는 문자열을 괄호로 묶고 뒤에 {개수} 형식을 지정합니다.

print(re.match('h{3}','hhhello')) 
# <re.Match object; span=(0, 3), match='hhh'>
print(re.match('(hello){3}', 'hellohellohelloworld'))
# <re.Match object; span=(0, 15), match='hellohellohello'>

#특정 범위의 문자(숫자)가 몇 개 있는지 판단할 수도 있습니다. 이때는 범위 [ ] 뒤에 {개수} 형식을 지정합니다.
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}','010-1000-1000')) #숫자 3개-4개-4개 패턴에 매칭됨
# <re.Match object; span=(0, 13), match='010-1000-1000'>
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}','010-1000-100')) #숫자 3개-4개-4개 패턴에 매칭되지 않음
# None

## 이 기능은 문자(숫자)의 개수 범위도 지정할 수 있습니다. 
# {시작개수,끝개수} 형식으로 시작 개수와 끝 개수를 지정해주면 특정 개수 사이에 들어가는지 판단합니다.

print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}','02-100-1000')) # 2~3개 - 3~4개 - 4개 패턴에 매칭됨
# <re.Match object; span=(0, 11), match='02-100-1000'>
print(re.match('[A-Z]{2}-[0-9]{2}-[0-9]{4}-[0-9]{4}','KR-10-1111-1111'))


##지금까지 숫자 범위만 판단해보았으니 이제 숫자와 영문 문자를 조합해서 판단해보겠습니다. 영문 문자 범위는 a-z, A-Z와 같이 표현합니다.
print(re.match('[a-zA-Z0-9]+','Hello1234')) # a부터 z, A부터 Z, 0부터 9까지 1개 이상 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 9), match='Hello1234'>
print(re.match('[A-Z0-9]+','hello')) # 대문자, 숫자는 없고 소문자만 있으므로 패턴에 매칭되지 않음
# None


##특정 문자 범위에 포함되지 않는지 판단하려면 어떻게 해야 할까요? 다음과 같이 문자(숫자) 범위 앞에 ^를 붙이면 해당 범위를 제외합니다.

print(re.match('[^A-Z]+','Hello')) # 대문자를 제외, 대문자가 있으므로 패턴에 매칭되지 않음
print(re.match('[^A-Z]+','hello')) # 대문자를 제외, 대문자가 없으므로 패턴에 매칭됨
# <re.Match object; span=(0, 5), match='hello'>

# 앞에서 특정 문자열로 시작하는지 판단할 때도 ^를 사용했었는데 문법이 비슷해서 이 부분은 헷갈리기 쉽습니다. 
# 범위를 제외할 때는 '[^A-Z]+'와 같이 [ ] 안에 넣어주고, 특정 문자 범위로 시작할 때는 '^[A-Z]+'와 같이 [ ] 앞에 붙여줍니다.
#  그래서 다음과 같이 '^[A-Z]+'는 영문 대문자로 시작하는지 판단합니다.

print(re.search('^[A-Z]+','Hello')) #대문자로 시작하므로 패턴에 매칭됨
# <re.Match object; span=(0, 1), match='H'>

#물론 특정 문자(숫자) 범위로 끝나는지 확인할 때는 정규표현식 뒤에 $를 붙이면 됩니다.
print(re.search('[0-9]+$','Hello1234')) #숫자로 끝나므로 패턴에 매칭됨
# <re.Match object; span=(5, 9), match='1234'>

#문자열을 판단할 때 'Hello1234'처럼 평범한 문자열만 판단했습니다. 
# 그런데 정규표현식에 사용하는 특수 문자 *, +, ?, ., ^, $, (, ) [, ], - 등을 판단하려면 어떻게 해야 할까요? 
# 특수 문자를 판단할 때는 특수 문자 앞에 \를 붙이면 됩니다. 
# 단, [ ] 안에서는 \를 붙이지 않아도 되지만 에러가 발생하는 경우에는 \를 붙입니다.

print(re.search('\*+','1 ** 2')) # *이 들어 있는지 판단
#<re.Match object; span=(2, 4), match='**'>
print(re.match('[$()a-zA-Z0-9]+','$(document)')) # $,(,) 와 문자, 숫자가 들어 있는지 판단
# <re.Match object; span=(0, 11), match='$(document)'>

# \d: [0-9]와 같음. 모든 숫자
# \D: [^0-9]와 같음. 숫자를 제외한 모든 문자
# \w: [a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자
# \W: [^a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자를 제외한 모든 문자

print(re.match('\d+','1234')) # 모든 숫자이므로 패턴에 매칭됨
# <re.Match object; span=(0, 4), match='1234'>
print(re.match('\D+','Hello')) # 숫자를 제외한 모든 문자이므로 패턴에 매칭됨
# <re.Match object; span=(0, 5), match='Hello'>
print(re.match('\w+','Hello_1234')) #영문 대소문자, 숫자, 밑줄 문자이므로 패턴에 매칭됨
# <re.Match object; span=(0, 10), match='Hello_1234'>
print(re.match('\W+','(:)')) # 영문 대소문자, 숫자, 밑줄 문자를 제외한 모든 문자이므로 패턴에 매칭됨
# <re.Match object; span=(0, 3), match='(:)'>


#공백을 처리해보겠습니다. 공백은 ' '처럼 공백 문자를 넣어도 되고, \s 또는 \S로 표현할 수도 있습니다.
# \s: [ \t\n\r\f\v]와 같음. 공백(스페이스), \t(탭) \n(새 줄, 라인 피드), \r(캐리지 리턴), \f(폼피드), \v(수직 탭)을 포함
# \S: [^ \t\n\r\f\v]와 같음. 공백을 제외하고 \t, \n, \r, \f, \v만 포함

print(re.match('[a-zA-Z0-9 ]+','Hello 1234')) # ' '로 공백 표현
# <re.Match object; span=(0, 10), match='Hello 1234'>
print(re.match('[a-zA-Z0-9\s]+','Hello 1234')) # \s로 공백 표현
# re.Match object; span=(0, 10), match='Hello 1234'>

#매번 match나 search 함수에 정규표현식 패턴을 지정하는 방법은 비효율적입니다. 
# 같은 패턴을 자주 사용할 때는 compile 함수를 사용하여 정규표현식 패턴을 
# 객체로 만든 뒤 match 또는 search 메서드를 호출하면 됩니다.

p =re.compile('[0-9]+')
print(p.match('1234'))
# <re.Match object; span=(0, 4), match='1234'>
print(p.search('hello'))
# None