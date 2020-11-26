string, tmp, result = input(), "", ""
is_tag = False # 태그 진입시 True로 변합니다.

for i in string:
    if i == '<':
        is_tag = True
        result += tmp[::-1] + "<" # 지금까지 tmp에 들어있던 문자열을 역순으로 더해줍니다.
        tmp = ''
    elif i == '>':
        is_tag = False # 태그 밖으로 벗어나니 False로 변경합니다.
        result += ">"
    elif i == ' ':
        if is_tag: # 태그 안에서의 공백일 경우는 그냥 결과에 더해줍니다.
           result += ' '
        else: # 태그 밖에서 공백일 경우 그 전 공백 다음부터의 문자열을 역순으로 결과에 더해줍니다.
           result += tmp[::-1] + ' '
           tmp = ''
    else: # 위 세개를 제외한 일반 문자열들입니다.
        if is_tag: # 태그 안이면 그냥 바로 결과에 더해줍니다.
           result += i
        else: # 밖이면 나중에 거꾸로 뒤집기 위해 tmp에 넣어줍니다.
           tmp += i

result += tmp[::-1] # 마지막으로 나왔던 ' ' 다음에 나온 문자열들이 모여있습니다.
print(result)
