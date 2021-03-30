import re
# print(re.match('Hello','Hello, world'))
# # <re.Match object; span=(0, 5), match='Hello'>
# print(re.match('Python','Hello, world'))
# #None


# #문자열 앞에 ^를 붙이면 문자열이 맨 앞에 오는지 판단하고, 문자열 뒤에 $를 붙이면 문자열이 맨 뒤에 오는지 판단합니다
# # match 함수는 문자열 처음부터 매칭되는지 판단하지만, search함수는 문자열 일부분이 매칭되는지 판단한다.
# print(re.search('^Hello','Hello, world!'))
# # <re.Match object; span=(0, 5), match='Hello'>
# print(re.search('world!$','Hello, world!'))
# # <re.Match object; span=(7, 13), match='world!'>

# ##지정된 문자열이 하나라도 포함되는지 판단하기
# print(re.match('hello|world','hello'))
# #<re.Match object; span=(0, 5), match='hello'>

