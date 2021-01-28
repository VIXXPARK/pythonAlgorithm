import urllib.request, urllib.parse,urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) # decode: give me the byte string 
                                #and turn it into a Unicode character string.