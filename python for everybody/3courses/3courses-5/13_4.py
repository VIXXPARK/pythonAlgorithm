import xml.etree.ElementTree as ET
data ='''<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>''' ## ''' multi-line string
tree = ET.fromstring(data) ## 받은 스트링으로 트리 구조 형성 
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))

###     person
#       /   \
#     name  
#        \
#       chuck