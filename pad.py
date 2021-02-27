import re

def solution(files):

    def key_function(fn):
        head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
        return [head,int(number)]
    
    return sorted(files,key=lambda x: key_function(x.lower()))