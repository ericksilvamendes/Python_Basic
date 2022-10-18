

from msilib.schema import PublishComponent


class Forma:
    def __init__(self,area,perimetro):
        self.x = area
        self.y = perimetro

class Retangulo(Forma):
    def __init__(self, x, y):
        super().__init__(x, y)

    def calcularArea(self):
        Area = self.x * self.y
        return print(Area)
        
    def calcularPerimetro(self):
        Perimetro = 2*(self.x+self.y)
        return print(Perimetro)

class Triangulo(Forma):
    def __init__(self, area, perimetro):
        super().__init__(area, perimetro)
        

    def calcPerimetroDoTriangulo(self,altura):
        self.altura = altura
        perimetroDoTriangulo = self.x+self.y+ self.altura
        return print("Perímetro do Triangulo: ",perimetroDoTriangulo)
    
    def calcAreaDoTriangulo(self,altura):
        self.altura = altura
        areaDoTriangulo = (self.x*self.altura)*(0.5)
        return print("Àrea do Triangulo",areaDoTriangulo)

retangulo = Retangulo(10,10)
retangulo.calcularArea()

triangulo = Triangulo(10,10)
triangulo.calcPerimetroDoTriangulo(10)