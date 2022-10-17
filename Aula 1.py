


class Carro:
    def __init__(self):
        self._nrodas = 4


    def set_nrodas(self,n):
        self._nrodas = n

gol = Carro()
gol._nrodas
print(gol._nrodas)

gol.set_nrodas(6)
gol._nrodas
print(gol._nrodas)
########################################

class Parente():
    count = 0

    
    #construtor
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        Parente.count +=1
        
    def __str__(self):
        return "Name:{} Age {}".format(self.name,self.age)

p1 = Parente("Joao",10)
p2 = Parente("Maria",11)
p3 = Parente("",0)

p3.name = input()
p3.age = input()

print(p1)
print(p2)
print(p3)
print(Parente.count)
        