class Atleta:
    def __init__(self,aposentado,peso):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        if self.aposentado == True:
            print("Estou aposentado")
            return
        print("Estou na Ativa!")
        

        
