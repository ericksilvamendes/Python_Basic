from itertools import count


class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    

    def desconto(self,percentual):
        self.preco = self.preco-(self.preco*(percentual/100))
    
    def quantidadeP(self,quantidade):
        self.quantidade = quantidade
    
    @property #get
    def preco(self)    :
        return self._preco

    @preco.setter
    def preco(self,valor):
        if isinstance (valor ,str):
            valor = float (valor.replace('R$',''))
        
            self.preco = valor
    

p1 = Produto('Lapis', 12,2)
p2 = Produto('Caneta',80,2)
p1.desconto(10)
#p2.desconto(10)
#print(p1.desconto)


   