def solution1(numbers, hand):
    answer = ''
    flag=False
    if hand=='right':
        flag=True
    else:
        flag=False
    pad={}
    pad[1]='00'
    pad[2]='01'
    pad[3]='02'
    pad[4]='10'
    pad[5]='11'
    pad[6]='12'
    pad[7]='20'
    pad[8]='21'
    pad[9]='22'
    pad[0]='31'
    leftStart=[3,0]
    rightStart=[3,2]
    for number in numbers:
        if number in [1,4,7]:
            answer+='L'
            leftStart[0]=int(pad[number][0])
            leftStart[1]=int(pad[number][1])
        elif number in [3,6,9]:
            answer+='R'
            rightStart[0]=int(pad[number][0])
            rightStart[1]=int(pad[number][1])
        else:
            valX=int(pad[number][0])
            valY=int(pad[number][1])
            leftTotal=int(abs(leftStart[0]-valX))+int(abs(leftStart[1]-valY))
            rightTotal=int(abs(rightStart[0]-valX))+int(abs(rightStart[1]-valY))
            if leftTotal==rightTotal:
                if flag:
                    answer+='R'
                    rightStart[0]=int(pad[number][0])
                    rightStart[1]=int(pad[number][1])
                else:
                    answer+='L'
                    leftStart[0]=int(pad[number][0])
                    leftStart[1]=int(pad[number][1])
            else:
                if leftTotal<rightTotal:
                    answer+='L'
                    leftStart[0]=int(pad[number][0])
                    leftStart[1]=int(pad[number][1])
                else:
                    answer+='R'
                    rightStart[0]=int(pad[number][0])
                    rightStart[1]=int(pad[number][1])
        
    return answer

numbers=[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand="left"
print(solution1(numbers,hand))

################################################################
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer