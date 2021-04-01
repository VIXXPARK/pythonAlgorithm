height = [1,1]
lst=[[i,val] for i,val in enumerate(height)]
lst.sort(key=lambda x: -x[1])
init=lst[:2]
init.sort(key=lambda x: x[0])
left=init[0];right=init[1]
lst=lst[2:]
answer=min(left[1],right[1])*(right[0]-left[0])
for pair in lst:
    if pair[0]<left[0]:
        ground=right[0]-pair[0];xheight=min(pair[1],right[1])
        if answer<ground*xheight:
            answer=ground*xheight
            left=pair[:]
        elif answer==ground*xheight:
            left=pair[:]
    elif left[0]<pair[0]<right[0]:
        leftChangeGround=right[0]-pair[0];leftheight=min(pair[1],right[1])
        rightChangeGround=pair[0]-left[0];rightheight=min(left[1],pair[1])
        if leftChangeGround*leftheight<rightChangeGround*rightheight:
            if answer<rightChangeGround*rightheight:
                answer=rightChangeGround*rightheight
                left=pair[:]
        else:
            if answer<leftChangeGround*leftheight:
                answer=leftChangeGround*leftheight
                right=pair[:]
    else:
        ground=pair[0]-left[0];xheight=min(pair[1],left[1])
        if ground*xheight>answer:
            answer=ground*xheight
            right=pair[:]
        elif ground*xheight==answer:
            right=pair[:]
    


print(answer)