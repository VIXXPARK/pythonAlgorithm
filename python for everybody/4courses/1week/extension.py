class PartyAnimal:
    x=0
    name=''
    def __init__(self,name=''):
        self.name=name
        print(self.name)
    
    def party(self):
        self.x=self.x+1
        print(self.name,self.x)
    
class FootballFan(PartyAnimal):
    points=0
    def touchdown(self):
        self.points = self.points +7
        self.party()
        print(self.points,self.name,self.x)

s = PartyAnimal('Sally')
s.party()

j=FootballFan('Jim')
j.party()
j.touchdown()

