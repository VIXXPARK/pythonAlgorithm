class partyAnimal:
    x=0
    def __init__(self):
        print("I'm constructed")
    
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
    
    def __del__(self):
        print("I'm destructed",self.x)

an = partyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)