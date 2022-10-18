from email.mime import base
import Forma

ladoMaior = int (input("Digite o Lado Maior:"))
ladoMenor = int (input("Digite o Lado MEnor:"))
retangulo = (Forma.Retangulo(ladoMaior,ladoMenor))
retangulo.calcularArea()

baseDoTriangulo = int (input("Digite a Base Do Triangulo: "))
alturaDoTriangulo = int (input("Digite a Altura Do Triangulo:"))
triangulo = (Forma.Triangulo(10,10))
triangulo.calcAreaDoTriangulo(5)


