board=["x","b","w","x","w","b","b","w","b"]
y=iter(board)
def func(it:iter):
    try:
        head=next(it)
        if head=='b' or head == 'w':
            return head
        upperLeft=func(it)
        upperRight=func(it)
        lowerLeft=func(it)
        lowerRight=func(it)
        return "x"+lowerLeft+lowerRight+upperLeft+upperRight
    except:
        pass    
print(func(y))