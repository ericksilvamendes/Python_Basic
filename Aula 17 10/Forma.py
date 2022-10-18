

class Forma:
    def __init__(self,area,perimetro):
        self.area = area
        self.perimetro = perimetro

class Retangulo(Forma):
    def __init__(self, area, perimetro):
        super().__init__(area, perimetro)

    def calcularArea(self):
        Area = self.area * self.perimetro
        return print(Area)
        
    def calcularPerimetro(self):
        Perimetro = self.area+self.perimetro
        return print(Perimetro)

class Triangulo(Forma):
    def __init__(self, area, perimetro):
        super().__init__(area, perimetro)
        

    def calcPerimetroDoTriangulo(self,altura):
        self.altura = altura
        perimetroDoTriangulo = self.area+self.perimetro+ self.altura
        return print("Perímetro do Triangulo: ",perimetroDoTriangulo)
    
    def calcAreaDoTriangulo(self,altura):
        self.altura = altura
        areaDoTriangulo = (self.area*self.altura)*(0.5)
        return areaDoTriangulo

retangulo = Retangulo(10,10)
retangulo.calcularArea()

triangulo = Triangulo(10,10)
triangulo.calcPerimetroDoTriangulo(10)