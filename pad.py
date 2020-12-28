dot=123
ten=[1,10,100,1000,10000]
length=len(str(dot))
Lstr=(dot%1000)*10+(dot//1000)
Rstr=(dot%10)*ten[length-1]+(dot//10)
print(Lstr)