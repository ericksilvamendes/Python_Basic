class Ingresso:
    def __init__(self,valor):
        self.valor = valor
    
    def imprimirValor(self):
         
        print(f'Valor: {self.valor}')
        
a = Ingresso('100')
a.imprimirValor()

class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
    
    def addVip(self):
        self.valor_vip = self.valor+(self.valor*0.10)
        return print(f'Valor: {self.valor_vip}')

a = Ingresso(100)  
a.imprimirValor()

vip = Vip(100)
vip.addVip()

class Camarote(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
    
    def addCamarote(self):
        self.valor_camarote = self.valor+(self.valor*0.35)
        return print(f'Valor: {self.valor_camarote}')


camarote = Camarote(10)     
camarote.addCamarote()
a = Ingresso(100)  
a.imprimirValor()

